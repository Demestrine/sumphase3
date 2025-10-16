from app.database import SessionLocal
from app.models import User, Book, Genre

# Insert test user
session = SessionLocal()
new_user = User(name="Demmy", email="demmy@gmail.com")
session.add(new_user)
session.commit()
session.close()

# Query users
session = SessionLocal()
users = session.query(User).all()
for user in users:
    print(user.name, user.email)
session.close()
