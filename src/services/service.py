from abc import ABC
from sqlalchemy.orm import Session
from ..models.database import Base, BaseWithPK

class Service(ABC):
    __session_db: Session
    _model_type: type

    def __init__(self, session_db: Session, model_type: type):
        self.__session_db = session_db
        self._model_type = model_type
        if not issubclass(model_type, Base):
            raise Exception(f'can\'t init service with {model_type.__class__} as model_type (not a model)')

    # ---> CRUD.
    def create(self, model_to_add) -> bool:
        self.__session_db.add(model_to_add)
        self.__session_db.commit()
        self.__session_db.refresh(model_to_add)
        return True
    
    def readAll(self) -> list:
        return self.__session_db.query(self._model_type).all()

    def update(self, model_to_update) -> bool:
        self.__session_db.commit()
        self.__session_db.refresh(model_to_update)
        return True

    def delete(self, model_to_delete) -> bool:
        self.__session_db.delete(model_to_delete)
        self.__session_db.commit()
        return True
    

class ServiceWithPK(Service):

    def __init__(self, session_db: Session, model_type: type):
        super().__init__(session_db, model_type)
        if not issubclass(self._model_type, BaseWithPK):
            raise Exception(f'can\'t init service with {self._model_type.__class__} as model_type (no primary key)')

    def readById(self, model_id: int) -> any|None:
        return self.__session_db.query(self._model_type).filter(self._model_type.id == model_id).first()