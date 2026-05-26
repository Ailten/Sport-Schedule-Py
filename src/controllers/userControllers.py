from fastapi import APIRouter, Request, Depends, Form
from ..dto import UserLoginFormDto
from ..models import User
from ..dto import UserPrintDto, UserCreateDto, UserUpdateDto
from ..services import UserService
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

user_router = APIRouter(prefix='/user', tags=['User'])
template = Jinja2Templates(directory='src/views')


@user_router.get('/readAll')
def getAllUser(
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
    return RedirectResponse(url='/schedule/printMonth', status_code=303)

@user_router.get('/logout')
def logout(
    request: Request
):
    """
    Remove user in session, and redirect to login page.
    """
    # remove user from session.
    request.session.pop('user', None)

    return RedirectResponse(url='/user/login')
    
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

@user_router.get('/createAccount')
def createAccount(
    request: Request
):
    """
    Get page Create Account form.
    """
    return template.TemplateResponse(name='create_account.html', request=request)

@user_router.post('/createAccount')
def createAccount(
    request: Request, 
    user_form: UserCreateDto = Form(), 
    user_service: UserService=Depends(UserService.getService)
):
    """
    Create account and redirect to schedule page.
    """
    user = user_form.toUser()

    errors = []

    # error email unique.
    user_with_same_email = user_service.getUserByLogin(user.email)
    if user_with_same_email != None:
        errors.append({
            'title': 'Invalide Email',
            'message': 'there is already an account using this email !'
        })
    
    # error confirm password.
    if user_form.raw_password != user_form.confirm_password:
        errors.append({
            'title': 'Invalide Password',
            'message': 'your confirm password is not the same !'
        })

    # if create raise an error.
    if len(errors) > 0 :
        return template.TemplateResponse(name='create_account.html', request=request, context={
            'errors': errors,
            'user_params': user_form  # to re-fill form.
        })
    
    # create account.
    user_service.create(user)
    
    # save user in session.
    request.session['user'] = dict(UserPrintDto.fromUser(user))
    
    # redirect to schedule.
    return RedirectResponse(url='/schedule/printMonth', status_code=303)


@user_router.get('/updateAccount')
def updateAccount(
    request: Request,
    user_id: int|None = None,
    user_service: UserService=Depends(UserService.getService)
):
    """
    Get page Update Account form.
    """

    # get user_id from user log by default. 
    if user_id == None:
        user_id = request.session.get('user').get('id')

    user = user_service.readById(user_id)

    user_params = UserUpdateDto.fromUser(user)

    return template.TemplateResponse(name='update_account.html', request=request, context={
        'user_params': user_params,
        'user_params_email': user.email
    })

@user_router.post('/updateAccount')
def updateAccount(
    request: Request, 
    user_form: UserUpdateDto = Form(), 
    user_id: int|None = None,
    user_service: UserService=Depends(UserService.getService)
):
    """
    Update account and redirect to schedule page.
    """

    # take id user log by default.
    if user_id == None:
        user_id = request.session.get('user')['id']

    user = user_service.readById(user_id)
    
    if user == None:
        request.session['errors'] = [{
            'title': 'User Not Found',
            'message': 'The user you try to edit is not register !'
        }]
        RedirectResponse(url='/schedule/printMonth', status_code=303)

    # edit user take from DB, with value from form.
    user_form.fillUser(user)

    # update user.
    user_service.update(user)
    
    # save user in session.
    request.session['user'] = dict(UserPrintDto.fromUser(user))
    
    # redirect to schedule.
    return RedirectResponse(url='/schedule/printMonth', status_code=303)
