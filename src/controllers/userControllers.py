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


@user_router.get('/login')
def login(
    request: Request
):
    """
    get page login.
    """
    return template.TemplateResponse(name='login.html', request=request)

@user_router.post('/login')
def handleLogin(
    request: Request, 
    user_login_form: UserLoginFormDto = Form(), 
    user_service: UserService=Depends(UserService.getService),
):
    """
    Handle login form, to redirect to schedule (or back to login page with error).
    """
    user = user_service.getUserByLoginPassword(user_login_form.login, user_login_form.password)
    if not user:
        # TODO: send an error to the login view (to print in pop-up).
        return template.TemplateResponse(name='login.html', request=request)

    # save user in session.
    request.session['user'] = dict(UserPrintDto.fromUser(user))

    return template.TemplateResponse(name='schedule.html', request=request)

@user_router.post('/logout')
def logout(
    request: Request
):
    """
    Remove user in session, and redirect to login page.
    """
    # remove user from session.
    request.session.pop('user', None)

    return RedirectResponse(url="/user/login")
    

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