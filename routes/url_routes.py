from fastapi import APIRouter, Depends, HTTPException , Request
from sqlalchemy.orm import Session
from database import get_db
from schemas.url_schema import URLCreate, URLResponse
from services.url_service import create_short_url, get_original_url , get_url_analytics
from fastapi.responses import RedirectResponse
from models.click_model import Click
from services.url_service import get_trending_urls
from utils.url_rate_limiter import is_rate_limited

router = APIRouter(prefix="/url", tags=["URL"])

@router.post("/shorten")
def shorten_url(
    request: Request,
    data: URLCreate,
    db: Session = Depends(get_db)
):
    ip = request.client.host

    if is_rate_limited(ip):
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later."
        )

    return create_short_url(db, data)

    

@router.get("/clicks/{short_code}")
def get_clicks(short_code: str, db: Session = Depends(get_db)):
    from models.click_model import Click

    clicks = db.query(Click).filter(Click.short_code == short_code).all()

    return {
        "short_code": short_code,
        "total_clicks": len(clicks)
    }
    

@router.get("/analytics/{short_code}")
def analytics(short_code: str, db: Session = Depends(get_db)):
    data = get_url_analytics(db, short_code)

    if not data:
        raise HTTPException(status_code=404, detail="URL not found")

    return data

@router.get("/trending")
def trending_urls(db: Session = Depends(get_db)):
    return get_trending_urls(db)

@router.get("/{short_code}")
def redirect_url(short_code: str, request: Request, db: Session = Depends(get_db)):
    url = get_original_url(db, short_code)

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    click = Click(
        short_code=short_code,
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

    db.add(click)
    db.commit()
    return RedirectResponse(url=url.original_url, status_code=302)