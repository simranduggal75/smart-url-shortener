from models.url_model import URL
from utils.generator import generate_short_code
from models.click_model import Click
from sqlalchemy import func
from fastapi import HTTPException
from datetime import datetime, timedelta, timezone
def create_short_url(db, data):

   
    if data.custom_alias:
        existing = db.query(URL).filter(URL.short_code == data.custom_alias).first()

        if existing:
            raise HTTPException(status_code=400, detail="Custom alias already taken")

        short_code = data.custom_alias

    else:
        short_code = generate_short_code()
        
    eexpires_at = None
    if data.expires_in_minutes:
        expires_at = datetime.utcnow() + timedelta(minutes=data.expires_in_minutes)

    new_url = URL(
        original_url=data.original_url,
        short_code=short_code,
        expires_at=expires_at
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url


def get_original_url(db, short_code):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        return None

    
    if url.expires_at and url.expires_at < datetime.utcnow():
        raise HTTPException(status_code=410, detail="URL has expired")
       
    return url

def get_url_analytics(db, short_code):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        return None

    clicks = db.query(Click).filter(Click.short_code == short_code).all()

    return {
        "short_code": short_code,
        "total_clicks": len(clicks),
        "click_history": [
            {
                "ip_address": click.ip_address,
                "user_agent": click.user_agent,
                "timestamp": click.timestamp
            }
            for click in clicks
        ]
    }
    

def get_trending_urls(db, limit=5):
    results = db.query(
        Click.short_code,
        func.count(Click.id).label("clicks")
    ).group_by(Click.short_code)\
     .order_by(func.count(Click.id).desc())\
     .limit(limit)\
     .all()

    return [
        {"short_code": r.short_code, "clicks": r.clicks}
        for r in results
    ]