from dataclasses import dataclass
from ...models import CheckExercice
from datetime import date, datetime
from pydantic import BaseModel

#@dataclass
class CheckExerciceFormDto(BaseModel):
    id_exo_to_do: int
    date_exo: date
    date_checked: datetime

    def toCheckExercice(self) -> 'CheckExercice':
        return CheckExercice(
            exercice_to_do_id=self.id_exo_to_do,
            date_check=self.date_checked
        )