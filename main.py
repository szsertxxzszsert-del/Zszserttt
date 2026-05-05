import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

VIDEO = "https://gofile.io/d/fuycdD"

@app.get("/")
async def root():
    return {"status": "Zszserttt System Active"}

@app.get("/buy")
async def pay():
    return RedirectResponse(url=VIDEO)

@app.get("/health")
async def check():
    return {"status": "ok"}
