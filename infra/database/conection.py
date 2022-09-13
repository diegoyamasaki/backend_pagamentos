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

Session_Local = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)


Base = declarative_base()

@property
def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()