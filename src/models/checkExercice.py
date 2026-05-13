from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime, timezone

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exerciceToDo import ExerciceToDo

class CheckExercice(Base):
    
    # ---> FK and relations.
    exercice_to_do_id: Mapped[int] = mapped_column(ForeignKey('exercice_to_dos.id'))
    exercice_to_do: Mapped[ExerciceToDo] = relationship(
        foreign_keys=['user_id'], 
        back_populates='schedules_of_user', 
        init=False
    )

    # ---> parameters.
    date_check: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    #check_count: Mapped[int] = mapped_column(default=1)
