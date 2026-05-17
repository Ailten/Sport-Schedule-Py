from .database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as EnumSQL, CheckConstraint, ForeignKey
from datetime import date, timezone, datetime
from .gender import Gender

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from role import Role

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)

    # ---> FK and relations.
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))
    role: Mapped[Role] = relationship(
        foreign_keys=['role_id'], 
        back_populates='role_of_user', 
        init=False
    )

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
    
    # ---> constraints check.
    __table_args__ = {
        'email_format': CheckConstraint(r'email ~ \'^.*@.*\..*$\''),
        'phone_number_format': CheckConstraint(r'phone_number ~ \'^[0-9- ]*$\''),
        'height_min': CheckConstraint('height > 0'),
        'weight_min': CheckConstraint('weight > 0'),
        'birth_date_min': CheckConstraint('birth_date < CURRENT_DATE')
    }
    

