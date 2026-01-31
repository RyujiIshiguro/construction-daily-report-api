from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "建設現場日報システム API v0.1"}