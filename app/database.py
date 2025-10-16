# database connection and session setup

from sqlalchemy import create_engine
ffrom sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# replace the values with your PostgreSQL credentials
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "sumphase3"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

