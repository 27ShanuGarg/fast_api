# from app import FastAPI
from fastapi import APIRouter

user_router = APIRouter()

print('Hello')

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}    

class User:

    @user_router.get("/")
    async def root():
        return {"message": "Hello World"}

    @user_router.get("/users/", tags=["users"])
    async def read_users():
        return [{"username": "Rick"}, {"username": "Morty"}]

