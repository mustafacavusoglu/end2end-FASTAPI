#main.py

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

@app.get("/", response_class=UJSONResponse)
async def read_items():
    return [{"message": "Hello World from FastAPI"}]
