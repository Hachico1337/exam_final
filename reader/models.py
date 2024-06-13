from flask_sqlalchemy import SQLAlchemy
import datetime
from reader import db

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    year = db.Column(db.String(4))
    publisher = db.Column(db.String(255))
    author = db.Column(db.String(255))
    pages = db.Column(db.Integer)
    cover_id = db.Column(db.Integer, db.ForeignKey('covers.id'))
    cover = db.relationship('Covers')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Covers(db.Model):
    __tablename__ = 'covers'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    mime_type = db.Column(db.String(50))
    md5_hash = db.Column(db.String(32))

class Genres(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class BookGenres(db.Model):  
    __tablename__ = 'book_genres'
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), primary_key=True)
    book = db.relationship('Books', backref=db.backref('genres', lazy=True))
    genre = db.relationship('Genres', backref=db.backref('books', lazy=True))

class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rating = db.Column(db.Integer)
    text = db.Column(db.Text)
    added_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    book = db.relationship('Books', backref=db.backref('reviews', lazy=True))
    user = db.relationship('Users', backref=db.backref('reviews', lazy=True))

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    patronymic = db.Column(db.String(255))
    role_id = db.Column(db.Integer)

class Genre(db.Model):  # Исправлено название класса на Genre, предполагаю, что это опечатка
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)


