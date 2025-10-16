# handle user input and CRUD operations

from .database import session
from .models import User, Book, Genre

def run_cli():
    while True:
        print("\n1. add user")
        print("2. add book")
        print("3. view books")
        print("4. exit")
        choice = input("select an option: ")

        if choice == "1":
            name = input("enter user name: ")
            email = input("enter user email: ")
            session.add(User(name=name, email=email))
            session.commit()
            print("user added successfully")

        elif choice == "2":
            title = input("enter book title: ")
            author = input("enter book author: ")
            user_id = int(input("enter user id: "))
            genre_id = int(input("enter genre id: "))
            session.add(Book(title=title, author=author, user_id=user_id, genre_id=genre_id))
            session.commit()
            print("book added successfully")

        elif choice == "3":
            books = session.query(Book).all()
            for b in books:
                print(f"{b.id} | {b.title} | {b.author} | user id: {b.user_id} | genre id: {b.genre_id}")

        elif choice == "4":
            print("exiting CLI")
            break

        else:
            print("invalid option, try again")

