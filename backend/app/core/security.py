import bcrypt
from datetime import datetime, timedelta
import secrets
import string
from typing import Optional
from jose import jwt

SECRET_KEY = ''.join(secrets.choice(string.ascii_letters + string.digits + "!@#$%^&*(-_=+)") for _ in range(32))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1


# 验证密码
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


# 生成TOKEN
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        print('token所用的密钥:', SECRET_KEY, 'token所用的算法:', ALGORITHM)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print('解码后的token', payload)
        expiration = payload.get("exp")
        print('token的过期时间', expiration)
        if expiration is None:
            return False
        if datetime.utcnow() > datetime.utcfromtimestamp(expiration):
            return 'token过期'
        return True
    except jwt.JWTError:
        return 'token错误'
