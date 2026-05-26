from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone, date
from ..services import CheckExerciceService, ExerciceToDoService
from fastapi.responses import RedirectResponse


exercice_to_do_router = APIRouter(prefix='/exerciceToDo', tags=['exerciceToDo'])
template = Jinja2Templates(directory='src/views')


@exercice_to_do_router.post('/detailsWholeDay')
def schedule(
    request: Request,
    date_exo: date = Form(),
    user_id: int|None = None,
    exercice_to_do_service: ExerciceToDoService=Depends(ExerciceToDoService.getService)
):
    """
    Get page of details exercice for a day ask.
    """

    # default user id log.
    if user_id == None:
        user_id = request.session.get('user')['id']

    exercice_to_do = exercice_to_do_service.getAllForADay(date_exo)
    for etd in exercice_to_do:
        print([ ce.date_check.day for ce in etd.check_exercices ])
        
    return template.TemplateResponse(name='details_exo_to_do.html', request=request, context={
        'exercice_to_do': exercice_to_do
    })

    