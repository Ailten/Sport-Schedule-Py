from fastapi import APIRouter, Request, Depends, Form

from ..dto import UserLoginFormDto
from ..models import User, makeSession
from sqlalchemy.orm import Session as SqlSession
from ..dto import UserPrintDto, UserFormDto
from ..services import UserService
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

user_router = APIRouter(prefix='/user', tags=['User'])

template = Jinja2Templates(directory='src/views')


@user_router.get('/readAll')
async def getAllUser(
    request: Request, 
    user_service: UserService=Depends(UserService.getService),
) -> list[UserPrintDto]:
    """
    Get all Users.
    """
    return [ UserPrintDto.fromUser(u) for u in user_service.readAll() ]


@user_router.get('/readById')
def getUserById(
    request: Request, 
    user_id: int, 
    user_service: UserService=Depends(UserService.getService),
) -> User:
    """
    Get User by id.
    """
    return user_service.readById(user_id)


@user_router.get('/logIn')
def login(
    request: Request
):
    """
    Get User by login and password.
    """
    return template.TemplateResponse(name='login.html', request=request)

@user_router.post('/logIn')
def handleLogin(
    request: Request, 
    user_login_form: UserLoginFormDto = Form(), 
    user_service: UserService=Depends(UserService.getService),
):
    """
    Get User by login and password.
    """
    user = user_service.getUserByLoginPassword(user_login_form.login, user_login_form.password)
    if not user:
        # TODO: send an error to the login view (to print in pop-up).
        return template.TemplateResponse(name='login.html', request=request)

    # save user in session.
    request.session['user'] = dict(UserPrintDto.fromUser(user))

    return RedirectResponse('/user/readAll')
    

@user_router.post('/create')
def addUser(
    request: Request, 
    user_form: UserFormDto, 
    user_service: UserService=Depends(UserService.getService),
) -> User:
    """
    Create a new User.
    """
    user = user_form.toUser()
    user_service.create(user)
    return user