from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ...config.database import db_conn
from ...schemas import UserCreate, User

router = APIRouter()


@router.get("/")
async def default_route() -> dict[str, str]:
    return {"message": "Hello User!"}


@router.post("/signup", response_model= User)
async def signup(user: UserCreate, db: Session = Depends(db_conn)):
    pass    


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db_conn)
):
    pass
