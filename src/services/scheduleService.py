from .service import ServiceWithPK
from sqlalchemy.orm import Session
from ..models.schedule import Schedule
from datetime import date
import calendar

class ScheduleService(ServiceWithPK):

    def __init__(self, session_db: Session):
        super().__init__(session_db, Schedule)


    def getMonthOfAnUser(self, user_id: int, year: int, month: int) -> list[Schedule]:

        # get first and last day of month target.
        date_min_ask = date(year, month, 1)
        date_max_ask = date(year, month, calendar.monthrange(year, month)[1])

        return self._session_db.query(self._model_type).filter(
            self._model_type.user_id == user_id and
            (
                self._model_type.start_date <= date_max_ask and
                self._model_type.end_date >= date_min_ask
            )
        ).all()