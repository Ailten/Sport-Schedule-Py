from dataclasses import dataclass, asdict
from datetime import date
from ...models import Gender, User
import json

@dataclass
class UserPrintDto():
    id: int
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
            id=user.id,
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

    #def __dict__(self) -> dict[str, any]:
    #    user_dict = super().__dict__
    #    user_dict = { k:v for k,v in user_dict.items() if not callable(v) and not isinstance(v, (types.MethodType, types.FunctionType)) }  # drop method.
    #    user_dict['birth_date'] = self.birth_date.strftime('%d/%m/%Y')  # date to string.
    #    print(user_dict)
    #    return user_dict
    
    def __iter__(self):
        for k,v in self.__dict__.items():
            if callable(v):  # skip functions.
                continue

            try:
                json.dumps(v)
                yield k, v
            except(TypeError, OverflowError):  # skip parameter not serializable.
                continue
            
        yield 'birth_date', self.birth_date.strftime('%d/%m/%Y')  # date to string.
