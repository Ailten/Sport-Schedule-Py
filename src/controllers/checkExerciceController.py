from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone, date
from ..services import CheckExerciceService, ExerciceToDoService
from fastapi.responses import RedirectResponse
from ..dto import CheckExerciceFormDto
from ..utils import Permission


check_exercice_router = APIRouter(prefix='/checkExercice', tags=['checkExercice'])
template = Jinja2Templates(directory='src/views')


@check_exercice_router.post('/checkWholeDay')
def checkWholeDay(
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

    # take id user log by default.
    try:
        user_id = Permission.checkUserIdParam(user_id, request)
    except Exception as err:
        # redirect to schedule.
        request.session['errors'] = [{
            'title': repr(err),
            'message': repr(err)
        }]
        return RedirectResponse(url='/schedule/printMonth', status_code=303)

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


@check_exercice_router.post('/checkAnExo')
def checkAnExo(
    request: Request,
    check_exercice_form_dto: CheckExerciceFormDto,
    user_id: int|None = None,
    exercice_to_do_service: ExerciceToDoService=Depends(ExerciceToDoService.getService),
    check_exercice_service: CheckExerciceService=Depends(CheckExerciceService.getService)
):
    """
    Check an exercice to do.
    """

    # take id user log by default.
    try:
        user_id = Permission.checkUserIdParam(user_id, request)
    except Exception as err:
        # redirect to schedule.
        request.session['errors'] = [{
            'title': repr(err),
            'message': repr(err)
        }]
        return { 'is_success': False, 'redirect_url': '/exerciceToDo/detailsWholeDay' }
    
    # verify if exercice id is connected.
    exercice_to_do = exercice_to_do_service.readById(check_exercice_form_dto.id_exo_to_do)
    if exercice_to_do == None:
        request.session['errors'] = [{
            'title': 'No exercice found !',
            'message': 'No exercice found.'
        }]
        return { 'is_success': False, 'redirect_url': '/exerciceToDo/detailsWholeDay' }
    
    # verify if already check for this day.
    check_already = check_exercice_service.getByExoIdAndDate(
        check_exercice_form_dto.id_exo_to_do, 
        check_exercice_form_dto.date_exo
    )
    if check_already != None:
        request.session['errors'] = [{
            'title': 'Already check !',
            'message': 'Already check.'
        }]
        return { 'is_success': False, 'redirect_url': '/exerciceToDo/detailsWholeDay' }

    # verify date.
    if check_exercice_form_dto.date_exo != check_exercice_form_dto.date_checked.date:
        check_exercice_form_dto.date_checked = date(
            check_exercice_form_dto.date_exo.year, 
            check_exercice_form_dto.date_exo.month, 
            check_exercice_form_dto.date_exo.day
        )

    # create check_exercice.
    check_exercice = check_exercice_form_dto.toCheckExercice()
    check_exercice_service.create(check_exercice)
    
    return { 'is_success': True }

    



    