
import os
from dotenv import load_dotenv
from sqlalchemy import Column, ForeignKey, Table, create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column
import re

load_dotenv()

class Base(DeclarativeBase, MappedAsDataclass):
    @property
    def __tablename__(self):
        instance_name = self.__class__.__name__.lower()
        name_snake = re.sub(r'(.)([A-Z])', r'\1_\2', instance_name).lower()  # camel to snake case.
        return f'{name_snake}s'
    
class BaseWithPK(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

# create a connection (?).
#engine = create_engine(os.getenv('DB_URL'), echo=True)

# TODO: what does this line ?
#registrations = Table(
#    "registrations",
#    Base.metadata,
#    Column("tournament_id", ForeignKey("tournaments.id")),
#    Column("player_id", ForeignKey("players.id")),
#)