from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class AnalyzeRequest(BaseModel):
    sector: Optional[str] = None
    timeframe: Optional[str] = None
@app.get("/")
def home(name: Optional[str] = None, age: Optional[int] = None):
    return {
        "message": "GET request working",
        "name": name,
        "age": age
    }
@app.post("/analyze")
def analyze(data: AnalyzeRequest):
    return {
        "message": "POST request working",
        "sector": data.sector,
        "timeframe": data.timeframe
    }