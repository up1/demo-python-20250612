from fastapi import FastAPI
from hello import router as hello_router
from user import router as user_router
from track import router as track_router

# Create sqlite database and tables
from db import open_database, close_database
con = open_database()
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL UNIQUE,
            password TEXT,
            email TEXT)
    """) 
con.commit()
close_database(con)


# Create the FastAPI app
app = FastAPI()

# Include the hello router
app.include_router(hello_router)
app.include_router(user_router)
app.include_router(track_router)