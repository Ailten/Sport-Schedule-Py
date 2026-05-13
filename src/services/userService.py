from .service import ServiceWithPK
from sqlalchemy.orm import Session
from ..models.user import User
from passlib.context import CryptContext

class UserService(ServiceWithPK):
    __password_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self, session_db: Session):
        super().__init__(session_db, User)


    # override create, to hash password before.
    def create(self, user_to_add: User) -> User:
        password_hash = self.__password_hasher.hash(user_to_add.password)
        user_to_add.password = password_hash
        return super().create(user_to_add)

    def getUserByLogin(self, email: str) -> User|None:
        return self._session_db.query(User).filter(User.email == email).first()
    
    def getUserByLoginPassword(self, email: str, password: str) -> User|None:
        user_get = self.getUserByLogin(email)
        if user_get == None:
            return None
        if not self.__password_hasher.verify(password, user_get.password):
            return None
        return user_get
    


    