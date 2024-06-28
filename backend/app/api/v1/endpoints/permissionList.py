from fastapi import APIRouter, Request
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_token
from app.core.get_token import get_token
from app.crud.user import get_users_from_db
from app.models.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/permissionList")
async def get_permission_list(request: Request):
    print('收到了前台请求')
    token = get_token(request)
    print('前端传过来的token值', token)
    is_valid_token = verify_token(token)
    print('token是否有效?', is_valid_token)
    # token有效，开始获取数据
    if is_valid_token and is_valid_token != 'token过期' and is_valid_token != 'token错误':
        raw_users = get_users_from_db()
        print('获取到的权限列表数据：', raw_users)
        users = [
            User(
                user_id=user[0],
                name=user[1],
                createDate=user[2],
                department=user[3],
                role=user[4],
                phone=user[5],
                email=user[6],
                lastDate=user[7],
                lock=user[8] == 'True'
            )
            for user in raw_users
        ]
        print('数据格式转换后的权限列表数据：', users)
        return users
    # token过期
    elif is_valid_token == 'token过期':
        return {'Message': 'token过期'}
    elif is_valid_token == 'token错误':
        return {'Message': 'token错误'}
    # 打印请求的所有内容
