from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite://payment_database.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check-same_thread": False
    }
)

session_local = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)


Base = declarative_base()