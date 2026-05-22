
from fastapi import FastAPI, Request, APIRouter
from fastapi.staticfiles import StaticFiles
import src.controllers as controllers
from starlette.middleware import sessions 
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

app = FastAPI()

#app.add_middleware(sessions.SessionMiddleware(session_cookie=True, secret_key='secret_key_IDK'))
app.add_middleware(
    sessions.SessionMiddleware, 
    secret_key=os.getenv('STARLETTE_SECRET_KEY')
)

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


@app.get('/')
def index(
    request: Request
):
    """
    main endpoint, redirect to page login.
    """
    return RedirectResponse(url="/user/logIn")