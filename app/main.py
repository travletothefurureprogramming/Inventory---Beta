from fastapi import FastAPI
import uvicorn
from app.database import database
from app.routes import products

database.create_database()

app = FastAPI()
app.include_router(products.router)

@app.get("/")
def home():
    return {"message": "Inventory AI is running"}

if __name__ == "__main__":
    uvicorn.run("app.main:app")