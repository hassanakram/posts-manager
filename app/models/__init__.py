from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


from .post import Post
from .user import User
