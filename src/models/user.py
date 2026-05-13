from .database import BaseWithPK
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as EnumSQL, CheckConstraint
from datetime import date, timezone, datetime
from .gender import Gender

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from schedule import Schedule

class User(BaseWithPK):

    # ---> parameters.
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(hash=True)
    phone_number: Mapped[str] = mapped_column()
    height: Mapped[float] = mapped_column()
    weight: Mapped[float] = mapped_column()
    birth_date: Mapped[date] = mapped_column()
    gender: Mapped[Gender] = mapped_column(EnumSQL(Gender))

    # ---> calculated parameters.
    @property
    def age(self) -> int:
        today = datetime.now(timezone.utc).date()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    @property
    def imc(self) -> float:
        return self.weight / (self.height ** 2)
    

