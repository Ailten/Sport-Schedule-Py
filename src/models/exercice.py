from database import BaseWithPK
from sqlalchemy.orm import Mapped, mapped_column

class Exercice(BaseWithPK):

    # ---> parameters.
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    url_details: Mapped[str] = mapped_column()
    url_image: Mapped[str] = mapped_column()
    amplitude: Mapped[float] = mapped_column()
    is_minutes: Mapped[bool] = mapped_column()