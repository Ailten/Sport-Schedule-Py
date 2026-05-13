from database import BaseWithPK
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User

class Schedule(BaseWithPK):
    
    # ---> FK and relations.
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped[User] = relationship(
        foreign_keys=['user_id'], 
        back_populates='schedules_of_user', 
        init=False
    )

    # ---> parameters.
    start_date: Mapped[date] = mapped_column()
    end_date: Mapped[date] = mapped_column(nullable=True, default=None)