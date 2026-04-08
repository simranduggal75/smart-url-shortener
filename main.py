from fastapi import FastAPI
from database import Base, engine
from routes.url_routes import router as url_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(url_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart URL Shortener API!"}