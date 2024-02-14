from fastapi import FastAPI
from app.api import routers
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(routers.router, prefix="/api", tags=["api"])
