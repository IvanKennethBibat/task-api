from fastapi import FastAPI
from app.database import engine
from app import models, routes, user_routes
from prometheus_fastapi_instrumentator import Instrumentator

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

Instrumentator().instrument(app).expose(app)

app.include_router(routes.router)
app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "task-api is running"}

@app.get("/health")
def health():
    return {"status": "ok"}