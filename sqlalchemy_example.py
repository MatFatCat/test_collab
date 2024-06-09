from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customers(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)


engine = create_engine('postgresql://matthewpopov:12345678@127.0.0.1/test')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

customers = session.query(Customers).all()

for customer in customers:
    print(customer.name)


session.close()
