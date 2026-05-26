from .database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.ext.hybrid import hybrid_method
from .daysOfWeek import DaysOfWeek

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .schedule import Schedule
    from .exercice import Exercice
    from .checkExercice import CheckExercice

class ExerciceToDo(Base):
    __tablename__ = 'exercice_to_dos'
    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    # ---> FK and relations.
    schedule_id: Mapped[int] = mapped_column(ForeignKey('schedules.id'))
    schedule: Mapped[Schedule] = relationship(
        back_populates='exercice_to_dos',
        init=False
    )
    exercice_id: Mapped[int] = mapped_column(ForeignKey('exercices.id'))
    exercice: Mapped[Exercice] = relationship(
        init=False
    )
    check_exercices: list['CheckExercice'] = relationship(back_populates='exercice_to_do')

    # ---> parameters.
    days_of_week: Mapped[int] = mapped_column()
    repetition: Mapped[int] = mapped_column(default=3)
    series: Mapped[int] = mapped_column(default=8)
    additional_weight: Mapped[float] = mapped_column(default=0.0)
    
    # ---> constraints check.
    #__table_args__ = {
    #    'days_of_week_range': CheckConstraint('days_of_week BETWEEN 1 AND 127 '),
    #    'repetition_min': CheckConstraint('repetition > 0 '),
    #    'series_min': CheckConstraint('series > 0 ')
    #}

    @hybrid_method
    def has_day_of_week(self, day_of_week: 'DaysOfWeek'):
        return (self.days_of_week & day_of_week) == day_of_week