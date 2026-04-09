from models.url_model import URL
from utils.generator import generate_short_code
from models.click_model import Click

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