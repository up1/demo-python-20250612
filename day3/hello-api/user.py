from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from db import open_database, close_database
import sqlite3


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
    import hashlib
    user.password = hashlib.sha256(user.password.encode()).hexdigest()

    # save user to database
    try:
        con = open_database()
        cur = con.cursor()
        print(user.model_dump(exclude={"password"}))
        cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (user.name, user.email, user.password))
        con.commit()
        close_database(con)

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        close_database(con)

