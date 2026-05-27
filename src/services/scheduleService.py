from .service import ServiceWithPK
from sqlalchemy.orm import Session, contains_eager
from ..models import Schedule, CheckExercice, ExerciceToDo
from datetime import date
import calendar
from sqlalchemy.sql import and_, or_

class ScheduleService(ServiceWithPK):

    def __init__(self, session_db: Session):
        super().__init__(session_db, Schedule)


    def getMonthOfAnUser(self, user_id: int, year: int, month: int) -> list[Schedule]:

        # get first and last day of month target.
        date_min_ask = date(year, month, 1)
        date_max_ask = date(year, month, calendar.monthrange(year, month)[1])

        # get max date for end check exercice (+24h).
        date_max_ask_check = date(year, month + 1, 1)

        return self._session_db.query(
            Schedule
        ).join(
            ExerciceToDo
        ).join(  # fake outer join.
            CheckExercice,
            CheckExercice.exercice_to_do_id == ExerciceToDo.id and (  # 
                CheckExercice.date_check < date_max_ask_check,
                CheckExercice.date_check >= date_min_ask
            ),
            isouter=True
        ).filter(
            and_(
                self._model_type.user_id == user_id,

                self._model_type.start_date <= date_max_ask,
                or_(
                    Schedule.end_date == None,
                    Schedule.end_date >= date_min_ask
                )
            )
        ).all()


# TODO: make proper outer join.
#.outerjoin(
#    CheckExercice
#).filter(
#    or_(
#        CheckExercice.id == None,
#        and_(
#            CheckExercice.date_check < date_max_ask_check,
#            CheckExercice.date_check >= date_min_ask
#        )
#).options(
#    contains_eager(Schedule.exercice_to_dos).contains_eager(ExerciceToDo.checkExecercices)
#)
    

    def getCurrentScheduleOfAnUser(self, user_id: int) -> Schedule|None:
        return self._session_db.query(self._model_type).filter(
            self._model_type.user_id == user_id and
            self._model_type.end_date == None
        ).first()