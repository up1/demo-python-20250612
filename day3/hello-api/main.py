from fastapi import FastAPI
from hello import router as hello_router
from user import router as user_router

# Create sqlite database and tables
import sqlite3
con = sqlite3.connect("users.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL UNIQUE,
            password TEXT,
            email TEXT)
    """) 
con.commit()
con.close()


# Create the FastAPI app
app = FastAPI()

# Include the hello router
app.include_router(hello_router)
app.include_router(user_router)