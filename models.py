from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)


user_car = Table(
    'user_car', Base.metadata,
    Column('user_id', ForeignKey('users.id')),
    Column('car_id', ForeignKey('cars.id')),
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())

    review = relationship('Review', back_populates='user')
    cars = relationship('Car', secondary='user_car', back_populates='users')

    def __repr__(self):
        return f'Name: {self.name}'


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer(), primary_key=True)
    image = Column(String())
    brand = Column(String())
    model = Column(String())
    year = Column(Integer())
    mileage = Column(Integer())
    price = Column(Integer())
    cc = Column(Integer())
    usage = Column(String())
    drive = Column(String())
    description = Column(String())
    

    review = relationship('Review', back_populates='cars')
    users = relationship('User', secondary='user_car', back_populates='cars')

    def __repr__(self):
        return f'Model: {self.model}, Year: {self.year}'


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    review = Column(String())

    user_id = Column(Integer(), ForeignKey('users.id'))
    car_id = Column(Integer(), ForeignKey('cars.id'))

    cars = relationship('Car', back_populates='review')
    user = relationship('User', back_populates='review')

    def __repr__(self):
        return f'Review: {self.review}'
