from .service import ServiceWithPK
from sqlalchemy.orm import Session
from ..models import ExerciceToDo, Schedule, CheckExercice
from datetime import date
import calendar
from sqlalchemy.sql import and_, or_
from sqlalchemy import cast, Date as SqlDate

class ExerciceToDoService(ServiceWithPK):

    def __init__(self, session_db: Session):
        super().__init__(session_db, ExerciceToDo)


    # get all exerciceToDo, for a date ask (wish is not already checked).
    def getAllForADayNotChecked(self, date_ask: date) -> list['ExerciceToDo']:

        days_befor_month, _ = calendar.monthrange(date_ask.year, date_ask.month)
        day_of_week = (date_ask.day + days_befor_month - 1) % 7
        day_week_enum = 2**day_of_week

        return self._session_db.query(self._model_type).join(
            Schedule
        ).join(
            CheckExercice,
            and_(
                CheckExercice.exercice_to_do_id == ExerciceToDo.id, 
                cast(CheckExercice.date_check, SqlDate) == date_ask
            ),
            isouter=True
        ).filter(
            and_(
                # take only thos who's not already checked.
                CheckExercice.id == None,

                # byte compare day of week.
                ExerciceToDo.days_of_week.op("&")(day_week_enum) > 0,

                Schedule.start_date <= date_ask,
                or_(
                    Schedule.end_date == None, 
                    Schedule.end_date >= date_ask
                )
            )
        ).all()
    

    def getAllForADay(self, user_id: int, date_ask: date) -> list['ExerciceToDo']:

        days_befor_month, _ = calendar.monthrange(date_ask.year, date_ask.month)
        day_of_week = (date_ask.day + days_befor_month - 1) % 7
        day_week_enum = 2**day_of_week

        return self._session_db.query(self._model_type).join(
            Schedule
        ).join(
            CheckExercice,
            and_(
                CheckExercice.exercice_to_do_id == ExerciceToDo.id, 
                cast(CheckExercice.date_check, SqlDate) == date_ask
            ),
            isouter=True
        ).filter(
            and_(
                Schedule.user_id == user_id,

                # byte compare day of week.
                ExerciceToDo.days_of_week.op("&")(day_week_enum) > 0,

                Schedule.start_date <= date_ask,
                or_(
                    Schedule.end_date == None, 
                    Schedule.end_date >= date_ask
                )
            )
        ).all()

