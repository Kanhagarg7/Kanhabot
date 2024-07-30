import uvicorn
import os
import requests
import json
import base64
import re
import logging
from typing import Union
from base64 import b64decode

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pydantic import BaseModel
from loguru import logger
import nest_asyncio

LibsicXInstall = os.getenv("LibsicXInstall")
os.system(f"pip3 install -q {LibsicXInstall}")

logging.basicConfig(level=logging.ERROR)

app = FastAPI(
 title="HellBot",
 version="1.0.2",
 contact={
  "name": "🌀ʊʄ⊕ք🌀",
  "url": "https://t.me/UFoPinfo",
 },
 docs_url=None, redoc_url="/"
)

class UserRequestIn(BaseModel):
    text: str

@app.post("/test")
def index(request: UserRequestIn):
    logger.debug(request)
    return {"ok": True}

@app.get("/")
def HellBot():
    return {"message": "running"}

if __name__ == "__main__":
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=7860)
