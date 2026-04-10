from pydantic import BaseModel
from typing import Optional
class URLCreate(BaseModel):
    original_url: str
    custom_alias: Optional[str] = None
    expires_in_minutes: Optional[int] = None
class URLResponse(BaseModel):
    id: int
    original_url: str
    short_code: str

    class Config:
        from_attributes = True