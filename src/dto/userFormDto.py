from dataclasses import dataclass 
from datetime import date
from ..models import Gender, User


@dataclass
class UserFormDto():

    first_name: str
    last_name: str
    email: str
    phone_number: str
    height: float
    weight: float
    birth_date: date
    gender: Gender
    #url_profil_picture: str

    raw_password: str

    def toUser(self) -> User:
        return User(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone_number=self.phone_number,
            height=self.height,
            weight=self.weight,
            birth_date=self.birth_date,
            gender=self.gender,
            #url_profil_picture=self.url_profil_picture,
            url_profil_picture=None,
            
            password=self.raw_password,  # hash in create service.
            role_id=1  # role Client, by default.
        )
