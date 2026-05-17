
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Role(Base):
    __tablename__ = 'roles'
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # ---> parameters.
    name: Mapped[str] = mapped_column(unique=True)