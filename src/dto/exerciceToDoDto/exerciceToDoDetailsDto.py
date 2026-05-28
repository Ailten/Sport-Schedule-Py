from dataclasses import dataclass
from ...models.exerciceToDo import ExerciceToDo
from datetime import date

@dataclass
class ExerciceToDoDetailsDto():
    id: int
    exercice_name: str
    days_of_week: int
    repetition: int
    series: int
    additional_weight: float

    check: bool  # dto for one day.

    @staticmethod
    def fromExerciceToDo(exerciceToDo: 'ExerciceToDo', date_day: date) -> 'ExerciceToDoDetailsDto':
        return ExerciceToDoDetailsDto(
            id=exerciceToDo.id,
            exercice_name=exerciceToDo.exercice.name,
            days_of_week=exerciceToDo.days_of_week,
            repetition=exerciceToDo.repetition,
            series=exerciceToDo.series,
            additional_weight=exerciceToDo.additional_weight,

            check = next([ True for etd in exerciceToDo.check_exercices if etd.date_check.date == date_day ].__iter__(), False)
        )

