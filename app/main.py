from fastapi import FastAPI
import uvicorn
from database import database

database.create_database()

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Inventory AI is running"}

if __name__ == "__main__":
    uvicorn.run("main:app")