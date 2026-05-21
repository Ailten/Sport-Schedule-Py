from .service import ServiceWithPK
from sqlalchemy.orm import Session
from ..models.exercice import Exercice

class ExerciceService(ServiceWithPK):

    def __init__(self, session_db: Session):
        super().__init__(session_db, Exercice)
