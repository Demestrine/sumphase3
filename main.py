from app.database import Base, engine, SessionLocal
from app.models import User, Book, Genre

# 1 Creates tables
Base.metadata.create_all(bind=engine)
print("Tables created in PostgreSQL successfully!")

# 2 Inserts test data
session = SessionLocal()
new_user = User(name="Demmy", email="demmy@gmail.com")
session.add(new_user)
session.commit()
session.close()
print("Test user added successfully!")

# 3 Querys data
session = SessionLocal()
users = session.query(User).all()
for user in users:
    print(user.name, user.email)
session.close()
