from fastapi import FastAPI
from app.api import routers

app = FastAPI()

app.include_router(routers.app, prefix="/api", tags=["api"])
