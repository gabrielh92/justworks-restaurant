import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.logger import logger

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M')

# init environment from local .env file
load_dotenv(override=True)

env = os.environ.get("ENVIRONMENT")
if env.upper() == "LOCAL":
    from src.models import seed
    seed()

# run server
logger.info(f"Running server on '{env}'")
server = FastAPI()
