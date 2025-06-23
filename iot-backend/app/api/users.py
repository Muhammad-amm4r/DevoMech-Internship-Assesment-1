from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.user import create_user, get_user_by_email, get_users
from app.schemas.user import UserCreate, User

router = APIRouter(tags=["users"])

@router.post("/", response_model=User)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(db, user)

@router.get("/", response_model=list[User])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db) 