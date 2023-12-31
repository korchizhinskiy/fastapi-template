from logging.config import dictConfig

from fastapi import FastAPI

from app.logging import LOGGING

app = FastAPI()

dictConfig(LOGGING)
