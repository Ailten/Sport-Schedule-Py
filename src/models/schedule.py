from .database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, CheckConstraint
from datetime import date

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User

class Schedule(Base):
    __tablename__ = 'schedules'
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    
    # ---> FK and relations.
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped[User] = relationship(
        init=False
    )

    # ---> parameters.
    start_date: Mapped[date] = mapped_column()
    end_date: Mapped[date] = mapped_column(nullable=True, default=None)
    
    # ---> constraints check.
    #__table_args__ = {
    #    'end_date_min': CheckConstraint('end_date = NULL OR end_date > start_date')
    #}