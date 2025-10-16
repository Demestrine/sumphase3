from .database import session
from .models import User, Book, Genre, Review, Publisher, Category

def show_menu():
    print("1. add user")
    print("2. add book")
    print("3. view books")
    print("4. add review")
    print("5. add publisher")
    print("6. add category")
    print("7. exit")

def add_user():
    name = input("enter user name: ")
    email = input("enter user email: ")
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print("user added successfully")

def add_genre(name):
    genre = Genre(name=name)
    session.add(genre)
    session.commit()
    return genre.id

def add_publisher():
    name = input("enter publisher name: ")
    publisher = Publisher(name=name)
    session.add(publisher)
    session.commit()
    print("publisher added successfully")

def add_category():
    name = input("enter category name: ")
    category = Category(name=name)
    session.add(category)
    session.commit()
    print("category added successfully")

def add_book():
    title = input("enter book title: ")
    author = input("enter book author: ")
    user_id = int(input("enter user id: "))
    genre_id = int(input("enter genre id: "))
    publisher_id = int(input("enter publisher id: "))
    category_id = int(input("enter category id: "))
    
    book = Book(title=title, author=author, user_id=user_id,
                genre_id=genre_id, publisher_id=publisher_id, category_id=category_id)
    session.add(book)
    session.commit()
    print("book added successfully")

def add_review():
    book_id = int(input("enter book id: "))
    user_id = int(input("enter user id: "))
    rating = int(input("enter rating 1-5: "))
    comment = input("enter comment: ")
    review = Review(book_id=book_id, user_id=user_id, rating=rating, comment=comment)
    session.add(review)
    session.commit()
    print("review added successfully")

def view_books():
    books = session.query(Book).all()
    for b in books:
        print(f"{b.id} | {b.title} | {b.author} | user id: {b.user_id} | genre id: {b.genre_id} | publisher id: {b.publisher_id} | category id: {b.category_id}")


