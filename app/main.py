from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "task-api is running lol"}

@app.get("/health")
def health():
    return {"status": "ok"}