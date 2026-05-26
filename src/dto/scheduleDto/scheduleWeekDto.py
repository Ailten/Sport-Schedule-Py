from dataclasses import dataclass
from ..exerciceToDoDto.exerciceToDoCalendarDto import ExerciceToDoCalendarDto
from ...models import DaysOfWeek
import calendar
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...models import Schedule

@dataclass
class ScheduleWeekDto():
    exercice_to_dos: list['ExerciceToDoCalendarDto']
    exercice_to_dos_keys: dict[list[int]]
    days_full_checked: list[int]

    @staticmethod
    def fromSchedule(schedule: 'Schedule', year: int, month: int) -> 'ScheduleWeekDto':
        output = ScheduleWeekDto(
            exercice_to_dos = [ ExerciceToDoCalendarDto.fromExerciceToDo(e) for e in schedule.exercice_to_dos ],
            exercice_to_dos_keys=dict(),
            days_full_checked=[]
        )
        output.__evalExerciceToDosKey()
        output.__evalDaysFullChecked(year, month)
        return output
    
    # map keys for exerciceToDos based on week day.
    def __evalExerciceToDosKey(self):

        self.exercice_to_dos_keys=dict()
        for i in range(len(DaysOfWeek)):
            day_of_week = DaysOfWeek(2**i)
            exercice_to_dos_keys_for_day_week = [ k for k,v in enumerate(self.exercice_to_dos) if (
                day_of_week in DaysOfWeek(v.days_of_week)
            ) ]
            if len(exercice_to_dos_keys_for_day_week) == 0:
                continue
            self.exercice_to_dos_keys[i] = exercice_to_dos_keys_for_day_week

    # map days who is full checked (all exo).
    def __evalDaysFullChecked(self, year:int, month: int):

        # get days in month ask.
        days_before_month, days_in_month = calendar.monthrange(year, month)

        for day_of_month in range(1, days_in_month + 1):
            day_of_week = (days_before_month + day_of_month - 1) % 7 + 1
            exo_keys = self.exercice_to_dos_keys[day_of_week - 1]
            exos = [ self.exercice_to_dos[ek] for ek in exo_keys ]
            exos_checked = [ e for e in exos if day_of_month in e.days_of_month_checked ]
            if len(exos_checked) == len(exos) and len(exos_checked) > 0:
                self.days_full_checked.append(day_of_month)

            
