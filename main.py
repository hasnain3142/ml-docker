import pytest
from fastapi import FastAPI, HTTPException
from model import model_inference

app = FastAPI()

@app.get("/")
def home():
    """Home endpoint"""
    return {"message": "Summarization Model Home"}

@app.post("/summarize")
async def summarize(data: dict):
    """Summarize endpoint"""
    if "text" not in data or not data["text"]:
        raise HTTPException(status_code=400, detail="Text input cannot be empty")
    summary = model_inference(data["text"])
    if not summary:
        raise HTTPException(status_code=500, detail="Failed to generate summary")
    return {"summary": summary}
