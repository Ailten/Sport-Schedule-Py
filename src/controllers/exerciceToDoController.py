from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone, date
from ..services import CheckExerciceService, ExerciceToDoService
from fastapi.responses import RedirectResponse
import calendar
from ..models import DaysOfWeek
from ..dto import ExerciceToDoDetailsDto
from ..utils import Permission


exercice_to_do_router = APIRouter(prefix='/exerciceToDo', tags=['exerciceToDo'])
template = Jinja2Templates(directory='src/views')


@exercice_to_do_router.post('/detailsWholeDay')
def scheduleDetailsDay(
    request: Request,
    date_exo: date = Form(),
    user_id: int|None = None,
    exercice_to_do_service: ExerciceToDoService=Depends(ExerciceToDoService.getService)
):
    """
    Get page of details exercice for a day ask.
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

    # get all exercice to do for a day.
    exercice_to_dos = exercice_to_do_service.getAllForADay(user_id, date_exo)

    # cast as DTO for filter data not need.
    exercice_to_dos_dto = [ ExerciceToDoDetailsDto.fromExerciceToDo(etd, date_exo) for etd in exercice_to_dos ]

    # get day str.
    days_skip_first_week, _ = calendar.monthrange(date_exo.year, date_exo.month)
    day_week_index = (days_skip_first_week + date_exo.day - 1) % 7
    day_week = DaysOfWeek(2**day_week_index).name

    context = {
        'date_ask': date_exo,
        'day_week': day_week,
        'date_ask_month': f'{date_exo.year}-{date_exo.month}', 
        'exercice_to_dos': exercice_to_dos_dto
    }

    errors = request.session.get('errors', None)  # include errors from redirction (if has one).
    if errors != None:
        context['errors'] = request.session.pop('errors')
        
    return template.TemplateResponse(name='details_exo_to_do.html', request=request, context=context)

    