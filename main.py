
from fastapi import FastAPI, Request, APIRouter
from fastapi.staticfiles import StaticFiles
import src.controllers as controllers
from src.models import makeSession

app = FastAPI()

app.mount('/public', StaticFiles(directory='src/public'), name='public')  # set folder public.

for item_name in dir(controllers):  # include all route controller.
   item = getattr(controllers, item_name)
   if isinstance(item, APIRouter):
       app.include_router(item)


@app.get('/ping')
def test(request: Request) -> dict:
    """
    Ping.
    """
    return { 'value': 'pong' }