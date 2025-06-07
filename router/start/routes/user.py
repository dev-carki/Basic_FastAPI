from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/user', tags=['user']) # prefix= 경로명

@router.get("/")
async def read_users():
    return [{"username": "Rickie"}, {"username": "Martin"}]


@router.get("/me")
async def read_user_me():
    return {"username": "currentuser"}


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}