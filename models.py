from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer(), primary_key=True)
    model = Column(String())
    year = Column(Integer())
    mileage = Column(Integer())
    price = Column(Integer())
    cc = Column(Integer())
    description = Column(String())

    brand = relationship('Brand', back_populates='cars')

    def __repr__(self):
        return f'Model: {self.model}, Year: {self.year}'


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer(), primary_key=True)
    brand = Column(String())

    cars = relationship('Brand', back_populates='brand')

    def __repr__(self):
        return f'Brand: {self.brand}'
