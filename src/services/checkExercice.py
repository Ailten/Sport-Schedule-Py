from service import Service
from sqlalchemy.orm import Session
from ..models.checkExercice import CheckExercice

class CheckExercice(Service):

    def __init__(self, session_db: Session):
        super().__init__(session_db, CheckExercice)
