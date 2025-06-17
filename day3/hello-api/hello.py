from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def say_hi():
    return {"message": "Hello world"}