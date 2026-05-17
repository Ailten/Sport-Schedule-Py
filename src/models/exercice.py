from .database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import CheckConstraint

class Exercice(Base):
    __tablename__ = 'exercices'
    id: Mapped[int] = mapped_column(primary_key=True)

    # ---> parameters.
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    url_details: Mapped[str] = mapped_column()
    url_image: Mapped[str] = mapped_column()
    amplitude: Mapped[float] = mapped_column()
    is_minutes: Mapped[bool] = mapped_column(default=False)
    
    # ---> constraints check.
    __table_args__ = {
        'name_format': CheckConstraint(r'name ~ \'[a-zA-Z_- ]{4,}\''),
        'url_details_format': CheckConstraint(r'url_details ~ \'^https://.*(.html)\''),
        'url_image_format': CheckConstraint(r'url_image ~ \'^https://.*(.png|.jpg|.jpeg|.webp)\''),
        #'amplitude_range': CheckConstraint('amplitude BETWEEN 0.0 AND 1.0')
        'amplitude_range': CheckConstraint('amplitude >= 0.0 AND amplitude <= 1.0')
    }
    #__table_args__ = (
    #    CheckConstraint('name ~ \'[a-zA-Z_- ]{4,}\'', name='name_format'),
    #    CheckConstraint('url_details ~ \'^https://.*(.html)\'', name='url_details_format'),
    #    CheckConstraint('url_image ~ \'^https://.*(.png|.jpg|.jpeg|.webp)\'', name='url_image_format'),
    #    CheckConstraint('amplitude BETWEEN 0.0 AND 1.0', name='amplitude_range')
    #)