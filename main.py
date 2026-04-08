from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Step 1 is wokring!!!"}