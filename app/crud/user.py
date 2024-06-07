from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_by_email(db: Session, email: str):
    return await db.query(models.User).filter(models.User.email == email).first()

async def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    await db.add(db_user)
    await  db.commit()
    await db.refresh(db_user)
    return db_user
