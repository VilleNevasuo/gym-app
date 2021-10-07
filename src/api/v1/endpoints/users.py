from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from dependencies import get_db
from models.User import User

router = APIRouter()


@router.get("/", tags=["users"])
async def read_users(db: Session = Depends(get_db)):    
    return db.query(User).all()


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
