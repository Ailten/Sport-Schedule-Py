import calendar
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from datetime import datetime
from ..services.scheduleService import ScheduleService
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

    context = {
        'month_ask': month_ask,  # string value, to assigne in input.
        'days_skip_first_week': days_skip_first_week, 
        'days_in_month': days_in_month,
        
        'today_day': today.day,  # numbers values, to comparate.
        'is_current_month': is_current_month,

        'schedules': schedules_use_in_month
    }
    errors = request.session.get('errors', None)  # include errors from redirction (if has one).
    if errors != None:
        del request.session['errors']
        context['errors'] = errors
    return template.TemplateResponse(name='schedule.html', request=request, context=context)

@schedule_router.get('/create')
def createSchedule(
    request: Request,
    schedule_service: ScheduleService=Depends(ScheduleService.getService)
):
    """
    Get page create a new Schedule.
    """
    # redirect to schedule.
    return template.TemplateResponse(name='create_schedule.html', request=request)

@schedule_router.get('/statistics')
def statistics(
    request: Request,
    schedule_service: ScheduleService=Depends(ScheduleService.getService)
):
    """
    Get page create a new Schedule.
    """
    # redirect to schedule.
    return template.TemplateResponse(name='statistics.html', request=request, context={

    })