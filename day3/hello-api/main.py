from fastapi import FastAPI
from hello import router as hello_router
from user import router as user_router

# Create the FastAPI app

app = FastAPI()

# Include the hello router
app.include_router(hello_router)
app.include_router(user_router)