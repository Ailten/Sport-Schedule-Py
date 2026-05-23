from datetime import date
from ...models import Gender, User
from pydantic import BaseModel
from dataclasses import dataclass


class UserUpdateDto(BaseModel):

    first_name: str
    last_name: str
    #email: str  # email and password can't be edited in menu, need a proper procedure with verification.
    phone_number: str
    height: float
    weight: float
    birth_date: date
    gender: int
    #url_profil_picture: str

    def fillUser(self, user: User):
        user.first_name = self.first_name
        user.last_name = self.last_name
        #user.email = self.email
        user.phone_number = self.phone_number
        user.height = self.height
        user.weight = self.weight
        user.birth_date = self.birth_date
        user.gender = Gender(self.gender)

    @staticmethod
    def fromUser(user: User) -> 'UserUpdateDto':
        return UserUpdateDto(
            first_name=user.first_name,
            last_name=user.last_name,
            #email=user.email,
            phone_number=user.phone_number,
            height=user.height,
            weight=user.weight,
            birth_date=user.birth_date,
            gender=user.gender.value
        )
    
    