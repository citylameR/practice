import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Book, Publisher, Shop, Stock, Sale

DSN = "postgresql://postgres:пароль@localhost:хост/БД"
engine = sqlalchemy.create_engine(DSN)

if __name__ == '__main__':
    create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

pub1 = Publisher(name="Булгаков")
pub2 = Publisher(name="Дюма")
session.add_all([pub1, pub2])
session.commit()

book1 = Book(title='Преступление и наказание', id_publisher=pub1.id)
book2 = Book(title='Граф Монте Кристо', id_publisher=pub2.id)
session.add_all([book1, book2])
session.commit()

sh1 = Shop(name="Читай город")
sh2 = Shop(name="Литрес")
session.add_all([sh1, sh2])
session.commit()

st1 = Stock(id_book=book1.id, id_shop=sh1.id, count=1000)
st2 = Stock(id_book=book2.id, id_shop=sh2.id, count=1000)
session.add_all([st1, st2])
session.commit()

sl1 = Sale(price=130, date_sale='28-10-2022', id_stock=st1.id, count=180)
sl2 = Sale(price=200, date_sale='29-12-2022', id_stock=st2.id, count=200)
session.add_all([sl1, sl2])
session.commit()

id = input('Введите фамилию либо id писателя: ')

if len(id) >= 3:
    result = session.query(Book, Shop, Sale).filter(Publisher.name == id).filter(
        Publisher.id == Book.id_publisher).filter(Book.id == Stock.id_book).filter(Stock.id_shop == Shop.id).filter(
        Stock.id == Sale.id_stock).all()
    for r in result:
        print(f'{r[0]} | {r[1]} | {r[2]}')
else:
    result = session.query(Book, Shop, Sale).filter(Publisher.id == id).filter(
        Publisher.id == Book.id_publisher).filter(Book.id == Stock.id_book).filter(Stock.id_shop == Shop.id).filter(
        Stock.id == Sale.id_stock).all()
    for r in result:
        print(f'{r[0]} | {r[1]} | {r[2]}')

session.close()
