from fastapi import APIRouter, Request, Depends
from ..models import User, makeSession
from sqlalchemy.orm import Session as SqlSession
from ..dto import UserPrintDto, UserFormDto
from ..services import UserService

user_router = APIRouter(prefix='/user')


@user_router.get('/readAll')
async def getAllUser(
    request: Request, 
    user_service: UserService=Depends(UserService.getService),
) -> list[UserPrintDto]:
    """
    Get all Users.
    """
    return [ UserPrintDto.fromUser(u) for u in user_service.readAll() ]


@user_router.post('/create')
def addUser(
    request: Request, 
    #user_form: UserFormDto, 
    user_service: UserService=Depends(UserService.getService),
) -> User:
    """
    Create a new User.
    """
    user = user_service.readById(1)
    user.password = 'Test1234'
    user.email = 'aaa.bbb@gmail.com'

    user_service.create(user)
    return user


@user_router.get('/readById')
def addUser(
    request: Request, 
    user_id: int, 
    user_service: UserService=Depends(UserService.getService),
) -> User:
    """
    Get User by id.
    """
    return user_service.readById(user_id)


@user_router.post('/logIn')
def addUser(
    request: Request, 
    user_login: str, 
    user_password_hash: str, 
    user_service: UserService=Depends(UserService.getService),
) -> User:
    """
    Get User by login and password.
    """
    return user_service.getUserByLoginPassword(user_login, user_password_hash)