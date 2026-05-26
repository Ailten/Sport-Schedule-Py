from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone, date
from ..services import CheckExerciceService, ExerciceToDoService
from fastapi.responses import RedirectResponse


check_exercice_router = APIRouter(prefix='/checkExercice', tags=['checkExercice'])
template = Jinja2Templates(directory='src/views')


@check_exercice_router.post('/checkWholeDay')
def schedule(
    request: Request,
    date_exo: date = Form(),
    user_id: int|None = None,
    date_check: datetime|None = None,
    check_exercice_service: CheckExerciceService=Depends(CheckExerciceService.getService),
    exercice_to_do_service: ExerciceToDoService=Depends(ExerciceToDoService.getService)
):
    """
    Check a whole day of exercice.
    """

    # default user.
    if user_id == None:
        user_id = request.session.get('user')['id']

    # default date check now.
    if date_check == None:
        date_check = datetime.now(timezone.utc)

    # date check should be in day of exercice_to_do !
    if date_check.date != date_exo:
        date_check = datetime(date_exo.year, date_exo.month, date_exo.day)

    exercices_to_dos = exercice_to_do_service.getAllForADay(date_exo)

    check_exercice_service.checkMany(exercices_to_dos, date_check)

    return RedirectResponse(url="/schedule/printMonth", status_code=303)


    