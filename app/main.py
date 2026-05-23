from fastapi import FastAPI
from app.database import engine
from app import models, routes, user_routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router)
app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "task-api is running"}

@app.get("/health")
def health():
    return {"status": "ok"}