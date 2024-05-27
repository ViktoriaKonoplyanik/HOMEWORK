from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

# Создание базы данных и сессии
engine = create_engine('sqlite:///bookstore.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Модели
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    books = relationship("Book", backref="author")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publication_year = Column(Integer)

    sales = relationship("Sale", backref="book")

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer)

# Создание таблиц
Base.metadata.create_all(engine)

# Дальнейший код остается без изменений


# Создание базы данных и сессии

# Задача 1: Создание и заполнение таблиц
# Добавление авторов
author1 = Author(first_name='John', last_name='Doe')
author2 = Author(first_name='Jane', last_name='Smith')
author3 = Author(first_name='Bob', last_name='Johnson')
session.add_all([author1, author2, author3])
session.commit()

# Добавление книг
book1 = Book(title='Book 1', author=author1, publication_year=2020)
book2 = Book(title='Book 2', author=author2, publication_year=2021)
book3 = Book(title='Book 3', author=author1, publication_year=2022)
book4 = Book(title='Book 4', author=author3, publication_year=2019)
session.add_all([book1, book2, book3, book4])
session.commit()

# Добавление продаж
sale1 = Sale(book=book1, quantity=10)
sale2 = Sale(book=book2, quantity=5)
sale3 = Sale(book=book3, quantity=8)
sale4 = Sale(book=book1, quantity=3)
sale5 = Sale(book=book4, quantity=2)
session.add_all([sale1, sale2, sale3, sale4, sale5])
session.commit()

# Задача 2: Использование JOIN
# INNER JOIN для получения списка всех книг и их авторов
books_and_authors = session.query(Book, Author) \
                          .join(Book.author) \
                          .all()

# LEFT JOIN для получения списка всех авторов и их книг
authors_and_books = session.query(Author, Book) \
                          .outerjoin(Author.books) \
                          .all()

# RIGHT JOIN для получения списка всех книг и их авторов
books_and_authors_right = session.query(Book, Author) \
                                .join(Book.author, isouter=True) \
                                .all()

# Задача 3: Множественные JOIN
# INNER JOIN для связывания таблиц authors, books и sales
books_authors_sales = session.query(Book, Author, Sale) \
                            .join(Book.author) \
                            .join(Book.sales) \
                            .all()

# LEFT JOIN для связывания таблиц authors, books и sales
authors_books_sales = session.query(Author, Book, Sale) \
                            .outerjoin(Author.books) \
                            .outerjoin(Book.sales) \
                            .all()


