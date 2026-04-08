from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.url_schema import URLCreate, URLResponse
from services.url_service import create_short_url, get_original_url

router = APIRouter(prefix="/url", tags=["URL"])

@router.post("/shorten", response_model=URLResponse)
def shorten_url(data: URLCreate, db: Session = Depends(get_db)):
    return create_short_url(db, data.original_url)


@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = get_original_url(db, short_code)

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return {"original_url": url.original_url}