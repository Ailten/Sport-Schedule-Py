from dataclasses import dataclass 
from datetime import date
from ..models import Gender, User

@dataclass
class UserPrintDto():
    first_name: int
    last_name: str
    email: str
    phone_number: str
    height: float
    weight: float
    birth_date: date
    gender: Gender
    url_profil_picture: str

    age: int
    imc: float
    role_name: str

    @staticmethod
    def fromUser(user: User) -> 'UserPrintDto':
        return UserPrintDto(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone_number=user.phone_number,
            height=user.height,
            weight=user.weight,
            birth_date=user.birth_date,
            gender=user.gender,
            url_profil_picture=user.url_profil_picture,

            age=user.age,
            imc=user.imc,
            role_name=user.role.name
        )
