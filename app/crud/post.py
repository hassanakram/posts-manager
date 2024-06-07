from typing import Any
from sqlalchemy.orm import Session
from . import models, schemas


async def create_post(db: Session, post: schemas.PostCreate, user_id: int) -> Any:
    db_post = models.Post(**post.dict(), owner_id=user_id)
    await db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post


async def get_posts(db: Session, user_id: int) -> list:
    return await db.query(models.Post).filter(models.Post.owner_id == user_id).all()


async def delete_post(db: Session, post_id: int, user_id: int) -> bool:
    db_post = await (
        db.query(models.Post)
        .filter(models.Post.id == post_id, models.Post.owner_id == user_id)
        .first()
    )
    if db_post:
        await db.delete(db_post)
        await db.commit()
        return True
    return False
