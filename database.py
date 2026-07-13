from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql//:root"

engine = create_engine(DATABASE_URL)

base = declarative_base()

sessionLocal = sessionmaker()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        

