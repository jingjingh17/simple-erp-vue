from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    name: str
    createDate: Optional[str] = None
    department: Optional[str] = None
    role: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    lastDate: Optional[str] = None
    lock: Optional[bool] = None
