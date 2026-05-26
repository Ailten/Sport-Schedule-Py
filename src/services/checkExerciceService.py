from .service import Service
from sqlalchemy.orm import Session
from ..models.checkExercice import CheckExercice
from ..models.exerciceToDo import ExerciceToDo
from datetime import datetime, timezone

class CheckExerciceService(Service):

    def __init__(self, session_db: Session):
        super().__init__(session_db, CheckExercice)

    
    # create a checkExercice (or update), for an ExerciceToDo.
    def checkAnExerciceToDo(self, exercice_to_do: ExerciceToDo, datetime_check: datetime|None=None) -> CheckExercice:
        if datetime_check != None:
            datetime_check = datetime.now(timezone.utc)

        checkExercice = CheckExercice(
            exercice_to_do_id = exercice_to_do.id,
            date_check=datetime_check
        )
        self.create(checkExercice)
        return checkExercice

    # create many checkExercice (matching to a list of exercice_to_do).
    def checkMany(self, exercice_to_dos: list['ExerciceToDo'], datetime_check: datetime):
        for etd in exercice_to_dos:
            checkExercice = CheckExercice(
                exercice_to_do_id = etd.id,
                date_check=datetime_check
            )
            self._session_db.add(checkExercice)
        self._session_db.commit()
        
        
