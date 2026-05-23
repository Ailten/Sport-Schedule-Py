from fastapi import APIRouter, Request, Depends, Form
from ..dto import UserLoginFormDto
from ..models import User
from ..dto import UserPrintDto, UserCreateDto
from ..services import UserService
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from datetime import datetime

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
        return template.TemplateResponse(name='login.html', request=request, context={
            'errors': [{
                'title': 'Access denied',
                'message': 'login or password incorrect !'
            }]
        })

    # save user in session.
    request.session['user'] = dict(UserPrintDto.fromUser(user))
    
    # redirect to schedule.
    return RedirectResponse(url="/schedule/printMonth", status_code=303)

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
    user_form: UserCreateDto, 
    user_service: UserService=Depends(UserService.getService),
) -> User:
    """
    Create a new User.
    """
    user = user_form.toUser()
    user_service.create(user)
    return user

@user_router.get('/createAcount')
def createAcont(
    request: Request
):
    """
    Get page Create Acount form.
    """
    return template.TemplateResponse(name='create_acount.html', request=request)

@user_router.post('/createAcount')
def createAcont(
    request: Request, 
    user_form: UserCreateDto = Form(), 
    user_service: UserService=Depends(UserService.getService)
):
    """
    Create acount and redirect to schedule page.
    """
    user = user_form.toUser()

    errors = []

    # error email unique.
    user_with_same_email = user_service.getUserByLogin(user.email)
    if user_with_same_email != None:
        errors.append({
            'title': 'Invalide Email',
            'message': 'there is already an acount using this email !'
        })
    
    # error confirm password.
    if user_form.raw_password != user_form.confirm_password:
        errors.append({
            'title': 'Invalide Password',
            'message': 'your confirm password is not the same !'
        })

    # if create raise an error.
    if len(errors) > 0 :
        return template.TemplateResponse(name='create_acount.html', request=request, context={
            'errors': errors,
            'user_params': user_form  # to re-fill form.
        })
    
    # create acount.
    user_service.create(user)
    
    # save user in session.
    request.session['user'] = dict(UserPrintDto.fromUser(user))
    
    # redirect to schedule.
    return RedirectResponse(url="/schedule/printMonth", status_code=303)
