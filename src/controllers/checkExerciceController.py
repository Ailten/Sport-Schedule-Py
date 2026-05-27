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

    # get all exercice to do (for a day specific AND whish is not checked already).
    exercices_to_dos = exercice_to_do_service.getAllForADayNotChecked(date_exo)

    check_exercice_service.checkMany(exercices_to_dos, date_check)
    
    # get last param month used.
    param_month = request.session.get('month_ask_schedule', '')
    if param_month != '':
        param_month = f'month_ask={param_month}'

    # reload with same month as the last ask (if has one).
    return RedirectResponse(url=f"/schedule/printMonth?{param_month}", status_code=303)


    