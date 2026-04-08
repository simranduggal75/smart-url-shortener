from models.url_model import URL
from utils.generator import generate_short_code

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
    return db.query(URL).filter(URL.short_code == short_code).first()