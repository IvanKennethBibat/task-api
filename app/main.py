from fastapi import FastAPI
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "task-api is running lol"}

@app.get("/health")
def health():
    return {"status": "ok"}