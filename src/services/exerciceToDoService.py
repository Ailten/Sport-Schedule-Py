from service import ServiceWithPK
from sqlalchemy.orm import Session
from ..models.exerciceToDo import ExerciceToDo

class ExerciceToDoService(ServiceWithPK):

    def __init__(self, session_db: Session):
        super().__init__(session_db, ExerciceToDo)
