from dataclasses import dataclass
from pydantic import BaseModel
from ...models.exerciceToDo import ExerciceToDo

@dataclass
class ExerciceToDoCreateDto():
    exercice_id: int
    days_of_week: int
    repetition: int
    series: int
    additional_weight: float

    def toExerciceToDo(self) -> 'ExerciceToDo':
        return ExerciceToDo(
            schedule_id=None,
            check_exercices=[],
            exercice_id=self.exercice_id,
            days_of_week=self.days_of_week,
            repetition=self.repetition,
            series=self.series,
            additional_weight=self.additional_weight
        )


class ListContainerExerciceToDoCreateDto(BaseModel):
    exercice_to_dos: list[ExerciceToDoCreateDto]

