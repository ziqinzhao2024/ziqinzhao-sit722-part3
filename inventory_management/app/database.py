from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://ziqinzhao_sit722_user:Uq8XE1sYnH5ScK6YWmRVxhOJ7VArCULq@dpg-crk30qaj1k6c73am8cc0-a.oregon-postgres.render.com/ziqinzhao_sit722" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
