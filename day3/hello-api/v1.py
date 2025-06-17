from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    name: str
    password: str
    email: str

app = FastAPI()

@app.post("/api/users", status_code=201)
def create_user(user: User):
    print(user)
    return {
        "id": 1,
        "name": "somkiat",
        "email": "somkiat@example.com"
    }

@app.get("/hello")
def say_hi():
    return {"message": "Hello world"}