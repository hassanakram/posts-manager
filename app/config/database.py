import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


async def db_conn() -> Session:
    engine = await create_engine('{}://{}:{}@{}/{}'.format(
        "mysql+pymysql",
        os.getenv("USERNAME"),
        os.getenv("PASSWORD"),
        os.getenv("HOST"),
        os.getenv("DATABASE")
    ), echo=False)
    Session = sessionmaker(bind=engine)
    return Session()
