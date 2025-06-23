from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://ammar:ammar@127.0.0.1:5434/mydatabase-pgresql"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)






