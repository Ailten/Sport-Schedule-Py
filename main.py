
from fastapi import FastAPI, Request, APIRouter, Depends
from fastapi.staticfiles import StaticFiles
import src.controllers as controllers
from starlette.middleware import sessions 
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv
from src.services import UserService, ScheduleService, ExerciceToDoService, CheckExerciceService

load_dotenv(dotenv_path='.env')

app = FastAPI()

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
    return { 'response': 'pong' }


@app.get('/')
def index(
    request: Request
):
    """
    main endpoint, redirect to page login.
    """
    return RedirectResponse(url="/user/login")


@app.get('/reset')
def test(
    request: Request,
    user_service: UserService=Depends(UserService.getService),
    schedule_service: ScheduleService = Depends(ScheduleService.getService),
    exercice_to_do_service: ExerciceToDoService = Depends(ExerciceToDoService.getService),
    check_exercice_service: CheckExerciceService = Depends(CheckExerciceService.getService),
) -> dict:
    """
    Reset DB for demo (remove end point in production).
    """

    # delete all schedules, exercices_to_do and check_exercice.
    schedules = schedule_service.readAll()
    for schedule in schedules:
        for etd in schedule.exercice_to_dos:
            for ce in etd.check_exercices:
                check_exercice_service.delete(ce)
            exercice_to_do_service.delete(etd)
        schedule_service.delete(schedule)

    # delete user for demo.
    user = user_service.getUserByLogin('email@gmail.com')
    if user != None:
        user_service.delete(user)
    
    return { 'response': 'Done' }