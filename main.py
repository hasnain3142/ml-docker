from typing import Union
from fastapi import FastAPI
from model import model_inference
from time import time

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/summarize")
def summarize(text: str):
    summary = model_inference(text)
    return {"summary": summary}
