from pydantic import BaseModel

class URLCreate(BaseModel):
    original_url: str

class URLResponse(BaseModel):
    id: int
    original_url: str
    short_code: str

    class Config:
        from_attributes = True