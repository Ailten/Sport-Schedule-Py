from .database import BaseWithPK
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .schedule import Schedule
    from .exercice import Exercice

class ExerciceToDo(BaseWithPK):

    # ---> FK and relations.
    schedule_id: Mapped[int] = mapped_column(ForeignKey('schedules.id'))
    schedule: Mapped[Schedule] = relationship(
        foreign_keys=['schedule_id'], 
        back_populates='exercice_to_do_for_schedule', 
        init=False
    )
    exercice_id: Mapped[int] = mapped_column(ForeignKey('exercices.id'))
    exercice: Mapped[Exercice] = relationship(
        foreign_keys=['exercice_id'], 
        back_populates='exercice_to_do_exercice', 
        init=False
    )

    # ---> parameters.
    days_of_week: Mapped[int] = mapped_column()
    repetition: Mapped[int] = mapped_column(default=3)
    series: Mapped[int] = mapped_column(default=8)
    additional_weight: Mapped[float] = mapped_column(default=0.0)