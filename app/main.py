from fastapi import FastAPI
from app.database import engine
from app import models, routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "task-api is running lol"}

@app.get("/health")
def health():
    return {"status": "ok"}