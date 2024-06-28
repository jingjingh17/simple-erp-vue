from fastapi import Request, HTTPException, status


# 获取前端传过来的TOKEN
def get_token(request: Request):
    authorization: str = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing or invalid",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 提取并打印 token 信息
    token = authorization.split(" ")[1]
    return token
