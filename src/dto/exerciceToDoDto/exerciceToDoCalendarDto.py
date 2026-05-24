from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...models.exerciceToDo import ExerciceToDo

@dataclass
class ExerciceToDoCalendarDto():
    exercice_name: str
    
    days_of_week: int
    repetition: int
    series: int
    additional_weight: float

    @staticmethod
    def fromExerciceToDo(exercice_to_do: 'ExerciceToDo') -> 'ExerciceToDoCalendarDto':
        return ExerciceToDoCalendarDto(
            exercice_name=exercice_to_do.exercice.name,

            days_of_week=exercice_to_do.days_of_week,
            repetition=exercice_to_do.repetition,
            series=exercice_to_do.series,
            additional_weight=exercice_to_do.additional_weight
        )