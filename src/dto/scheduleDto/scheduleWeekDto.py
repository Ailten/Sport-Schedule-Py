from dataclasses import dataclass
from ..exerciceToDoDto.exerciceToDoCalendarDto import ExerciceToDoCalendarDto
from ...models import DaysOfWeek
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...models import Schedule

@dataclass
class ScheduleWeekDto():
    exercice_to_dos: list['ExerciceToDoCalendarDto']
    exercice_to_dos_keys: dict[int, list[int]]

    @staticmethod
    def fromSchedule(schedule: 'Schedule') -> 'ScheduleWeekDto':
        output = ScheduleWeekDto(
            exercice_to_dos = [ ExerciceToDoCalendarDto.fromExerciceToDo(e) for e in schedule.exercice_to_dos ],
            exercice_to_dos_keys=dict()
        )
        output.__evalExerciceToDosKey()
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