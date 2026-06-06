from .database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime, timezone
from .exerciceToDo import ExerciceToDo

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass

class CheckExercice(Base):
    __tablename__ = 'check_exercices'
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    
    # ---> FK and relations.
    exercice_to_do_id: Mapped[int] = mapped_column(ForeignKey('exercice_to_dos.id'))
    exercice_to_do: Mapped[ExerciceToDo] = relationship(
        init=False,
        back_populates='check_exercices'
    )

    # ---> parameters.
    date_check: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
