from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# 現場名、担当者、内容、工数を定義する
class DailyReport(BaseModel):
    site_name: str
    reporter_name: str
    content: str
    work_hours: float

@app.get("/")
def read_root():
    return {"message": "建設現場日報システム API v1.0"}

@app.post("/reports/")
def create_report(report: DailyReport):
    # 本来はここでデータベースに保存する
    # 今は受信したデータに受信時刻をつけて返すだけ
    return {
        "status": "success",
        "received_at": datetime.now(),
        "data": report
    }
