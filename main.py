from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Smart URL Shortener API is running!!!"}