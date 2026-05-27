import calendar
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from datetime import datetime

from src.dto.scheduleDto.scheduleCalendarDto import ScheduleCalendarDto
from src.dto.scheduleDto.scheduleKcalDto import ScheduleKcalDto
from ..services import ScheduleService, ExerciceService, ExerciceToDoService
import re
from fastapi.responses import RedirectResponse


schedule_router = APIRouter(prefix='/schedule', tags=['Schedule'])
template = Jinja2Templates(directory='src/views')


@schedule_router.get('/')
def schedule(
    request: Request
):
    """
    Default route, redirect to schedule/printMonth
    """
    return RedirectResponse(url="/schedule/printMonth")

@schedule_router.get('/printMonth')
def printMonth(
    request: Request, 
    user_id: int|None = None, 
    month_ask: str|None = None,
    schedule_service: ScheduleService=Depends(ScheduleService.getService)
):
    """
    Get schedule of an user and render it on view schedule.
    """

    # take user log by default.
    if user_id == None:
        user_id = request.session.get('user').get('id')

    # take current month by default.
    if month_ask == None:
        month_ask = datetime.now().strftime('%Y-%m')
    year = int(re.search(r'^[0-9]{4}', month_ask).group(0))
    month = int(re.search(r'[0-9]{1,2}$', month_ask).group(0))
    days_skip_first_week, days_in_month = calendar.monthrange(year, month)

    # re defined month_ask (to avoid 1 char as month).
    zero_month = '0' if month < 10 else ''
    month_ask = f'{year}-{zero_month}{month}'

    # get today, for mark today in calendar.
    today = datetime.now()
    is_current_month = (
        today.month == month and
        today.year == year
    )

    # get all schedule for the month ask.
    schedules_use_in_month = schedule_service.getMonthOfAnUser(user_id, year, month)
    # cast in dto (to print easyli in view).
    schedules_calendar_dto = ScheduleCalendarDto.fromListSchedule(schedules_use_in_month, year, month)

    context = {
        'month_ask': month_ask,  # string value, to assigne in input.
        'days_skip_first_week': days_skip_first_week, 
        'days_in_month': days_in_month,
        
        'today_day': today.day,  # numbers values, to comparate.
        'is_current_month': is_current_month,

        'schedules_calendar': schedules_calendar_dto
    }
    errors = request.session.get('errors', None)  # include errors from redirction (if has one).
    if errors != None:
        del request.session['errors']
        context['errors'] = errors
    return template.TemplateResponse(name='schedule.html', request=request, context=context)

@schedule_router.get('/create')
def createSchedule(
    request: Request,
    exercice_service: ExerciceService=Depends(ExerciceService.getService)
):
    """
    Get page create a new Schedule.
    """

    # get all exercices from DB to use as dataset in view.
    exercices = [ {
        'id': e.id,
        'name': e.name
    } for e in exercice_service.readAll() ]

    return template.TemplateResponse(name='create_schedule.html', request=request, context={
        'exercices': exercices
    })

@schedule_router.post('/create')
async def createScheduleGetData(
    request: Request,
    exercice_to_do_service: ExerciceToDoService=Depends(ExerciceToDoService.getService)
):
    form_data = request.form()  # DEBUG.
    print(form_data)
    dict_data = dict(form_data)
    print(dict_data)
    
    return RedirectResponse(url="/schedule/printMonth")


@schedule_router.get('/statistics')
def statistics(
    request: Request,
    user_id: int|None = None,
    schedule_service: ScheduleService=Depends(ScheduleService.getService)
):
    """
    Get page statistics for the current schedule.
    """

    # default take id of user log.
    if user_id == None:
        user_id = request.session.get('user')['id']

    # get the last schedule of user (the one whith no date end)
    current_schedule = schedule_service.getCurrentScheduleOfAnUser(user_id)

    # cast as DTO object, to take only parameter whant (and print easyli).
    schedule_dto = ScheduleKcalDto.fromSchedule(current_schedule)

    # redirect to schedule.
    return template.TemplateResponse(name='statistics.html', request=request, context={
        'schedule': schedule_dto
    })