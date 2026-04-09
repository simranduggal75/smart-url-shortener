from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime , timezone

class Click(Base):
    __tablename__ = "clicks"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, ForeignKey("urls.short_code"))
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))