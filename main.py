# create tables, add default genres and users, start CLI

from app.database import engine, Base, session
from app.models import User, Genre, Book
from app.cli import run_cli

# create tables if they don't exist
Base.metadata.create_all(engine)

# add default genres if not already in db
default_genres = ["Fiction", "Non-fiction", "Science", "Mystery"]
for name in default_genres:
    if not session.query(Genre).filter_by(name=name).first():
        session.add(Genre(name=name))
session.commit()

# add default Kenyan users if not already in db
default_users = [
    {"name": "James Otieno", "email": "james.otieno@gmail.com"},
    {"name": "Mwaura Luke", "email": "mwaura.luke@gmail.com"},
    {"name": "Grace Mwikali", "email": "grace.mwikali@gmail.com"},
    {"name": "Demmy Awuor", "email": "demmy.awuor@gmail.com"}
]
for u in default_users:
    if not session.query(User).filter_by(email=u["email"]).first():
        session.add(User(name=u["name"], email=u["email"]))
session.commit()

# start CLI
run_cli()
