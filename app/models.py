from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

# users table
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    
    books = relationship("Book", back_populates="user")
    reviews = relationship("Review", back_populates="user")

# genres table
class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    books = relationship("Book", back_populates="genre")

# books table
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    user = relationship("User", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    reviews = relationship("Review", back_populates="book")
    publisher = relationship("Publisher", back_populates="books")
    category = relationship("Category", back_populates="books")

# reviews table
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer)
    comment = Column(Text)
    
    book = relationship("Book", back_populates="reviews")
    user = relationship("User", back_populates="reviews")

# publishers table
class Publisher(Base):
    __tablename__ = 'publishers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    books = relationship("Book", back_populates="publisher")

# categories table
class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    books = relationship("Book", back_populates="category")

