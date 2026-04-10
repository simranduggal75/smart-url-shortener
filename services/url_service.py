from models.url_model import URL
from utils.generator import generate_short_code
from models.click_model import Click
from sqlalchemy import func

def create_short_url(db, original_url):
    short_code = generate_short_code()

    new_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url


def get_original_url(db, short_code):
    url = db.query(URL).filter(URL.short_code == short_code).first()
    if url:
        click = Click(short_code=short_code)
        db.add(click)
        
        db.commit()
    return url

def get_url_analytics(db, short_code):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        return None

    total_clicks = db.query(func.count(Click.id))\
        .filter(Click.short_code == short_code).scalar()

    last_click = db.query(func.max(Click.timestamp))\
        .filter(Click.short_code == short_code).scalar()

    return {
        "short_code": short_code,
        "total_clicks": total_clicks,
        "last_clicked": last_click,
        "created_at": url.created_at
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