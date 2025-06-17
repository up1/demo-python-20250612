from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

class User(BaseModel):
    id: int | None = None
    name: str
    password: str
    email: EmailStr

@router.post("/api/users", status_code=201)
def create_user(user: User):
    # check username is unique
    # encrypt password with sha256 algorithm (md5 is not secure)
    # save user to database
    print(user.model_dump(exclude={"password"}))
    return {
        "id": 1,
        "name": "somkiat",
        "email": "somkiat@example.com"
    }