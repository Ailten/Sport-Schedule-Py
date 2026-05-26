from dataclasses import dataclass
from ...utils import Physics
from ...models import DaysOfWeek
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...models import Schedule

@dataclass
class ScheduleKcalDto():
    
    @staticmethod
    def fromSchedule(schedule: 'Schedule') -> list:
        output = []
        for i in range(7):
            
            # calcul joules use for all exo for a day.
            joules = sum([ (
                Physics.evalJoulesUseForExercice(
                    user = schedule.user, 
                    exercice = e.exercice, 
                    exercice_to_do = e
                )
            ) for e in schedule.exercice_to_dos if (
                DaysOfWeek(2**i) in DaysOfWeek(e.days_of_week)
            ) ])

            kcal = Physics.joulesToKcalories(joules)
            output.append(kcal)
        
        return output

