from service import ServiceWithPK
from sqlalchemy.orm import Session
from ..models.schedule import Schedule

class ScheduleService(ServiceWithPK):

    def __init__(self, session_db: Session):
        super().__init__(session_db, Schedule)
