from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models import auth
from app.core.security import verify_password, create_access_token
from app.crud.user import get_user_login_from_db
from datetime import timedelta

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/login")
def login_user(form_data: auth.Auth):
    print('收到的前台登录表单', form_data)
    print('收到的前台登录表单中的用户名', form_data.username)
    user = get_user_login_from_db(form_data.username)
    if user and verify_password(form_data.password, user[1]):
        access_token = create_access_token(data={"sub": user[0]}, expires_delta=timedelta(minutes=30))
        print('传给前端的token', access_token)
        return {"message": "Login successful", "access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
