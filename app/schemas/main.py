from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):
    pass


class PostBase(BaseModel):
    pass


class PostCreate(PostBase):
    pass


class Post(PostBase):
    pass
