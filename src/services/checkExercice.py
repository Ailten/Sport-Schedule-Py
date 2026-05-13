from service import Service
from sqlalchemy.orm import Session
from ..models.checkExercice import CheckExercice
from ..models.exerciceToDo import ExerciceToDo
from datetime import datetime

class CheckExerciceService(Service):

    def __init__(self, session_db: Session):
        super().__init__(session_db, CheckExercice)

    
    # create a checkExercice (or update), for an ExerciceToDo.
    def checkAnExerciceToDo(self, exercice_to_do: ExerciceToDo, datetime_check: datetime|None=None) -> bool:
        checkExercice = CheckExercice()
        if datetime_check != None:
            checkExercice.date_check = datetime_check
        self.create(checkExercice)
        
        
