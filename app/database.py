from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# PostgreSQL connection info
DATABASE_URL = "postgresql+psycopg2://postgres:Adrian12521@localhost:5432/sumphase3"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

