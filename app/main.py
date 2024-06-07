from fastapi import FastAPI
from .api.routes import posts, users

app = FastAPI()

# Import route functions from separate files
app.include_router(users.router, prefix="/api/user")
app.include_router(posts.router, prefix="/api/post")
