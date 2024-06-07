from fastapi import APIRouter
from ...schemas import Post

router = APIRouter()

@router.get("/")
async def default_route() -> dict[str, str]:
    return {"message": "Hello Post!"}

@router.post("/add-post", response_model=Post)
async def add_post():
    pass
   
@router.get("/get-posts", response_model=list[Post])
async def get_posts():
    pass

@router.delete("/delete-posts/{post_id}")
async def delete_post():
   pass
