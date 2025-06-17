from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from hello import router as hello_router

class User(BaseModel):
    id: int | None = None
    name: str
    password: str
    email: EmailStr

app = FastAPI()

# Include the hello router
app.include_router(hello_router)

@app.post("/api/users", status_code=201)
def create_user(user: User):
    # check username is unique
    # encrypt password with sha256 algorithm (md5 is not secure)
    # save user to database
    return {
        "id": 1,
        "name": "somkiat",
        "email": "somkiat@example.com"
    }