from dataclasses import dataclass
import calendar
from .scheduleWeekDto import ScheduleWeekDto
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...models import Schedule
    

@dataclass
class ScheduleCalendarDto():
    schedules: list['ScheduleWeekDto']
    schedules_keys: dict[int, int]

    @staticmethod
    def fromListSchedule(schedules : list['Schedule'], year, month) -> 'ScheduleCalendarDto':
        output = ScheduleCalendarDto(
            schedules=[ ScheduleWeekDto.fromSchedule(s) for s in schedules ],
            schedules_keys=dict()
        )
        output.__evalSchedulesKey(year, month, schedules)
        return output

    # get key dictionary to acces data easyli from view.
    def __evalSchedulesKey(self, year: int, month: int, schedules: list['Schedule']):

        # get days in month ask.
        _, days_in_month = calendar.monthrange(year, month)

        # generate key mapping for days of month.
        self.schedules_keys=dict()
        for i in range(days_in_month):
            key_schedule = next([ k for k,v in enumerate(schedules) if (
                v.start_date.day <= i and
                (v.end_date == None or v.end_date.day >= i)
            )].__iter__(), None)
            if key_schedule == None:  # skip if no schedule for this day.
                continue
            self.schedules_keys[i] = key_schedule