from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from models import Car, engine, User, Review, user_car

app = FastAPI()

# pydantic classes for cars


class Cartype(BaseModel):
    brand: str
    model: str
    year: int
    mileage: int
    price: int
    cc: int
    description: str


Session = sessionmaker(bind=engine)

# code to handle cars


@app.get('/cars', tags=['Cars'])
def get_cars():
    session = Session()
    cars = session.query(Car).all()
    session.close()
    return cars


@app.post('/cars', tags=['Cars'])
def add_car(car: Cartype):
    session = Session()
    car1 = Car(brand=car.brand, model=car.model, year=car.year, mileage=car.mileage,
               price=car.price, cc=car.cc, description=car.description)
    session.add(car1)
    session.commit()
    session.close()
    return 'Car added successfully'


@app.put('/cars/{id}', tags=['Cars'])
def edit_car(id: int, car: Cartype):
    session = Session()
    car1 = session.query(Car).filter_by(id=id).first()
    if car1:
        if car.brand:
            car1.brand = car.brand
        if car.model:
            car1.model = car.model
        if car.year:
            car1.year = car.year
        if car.mileage:
            car1.mileage = car.mileage
        if car.price:
            car1.price = car.price
        if car.cc:
            car1.cc = car.cc
        if car.description:
            car1.description = car.description

        session.commit()
        session.close()
        return 'Car updated successfully'
    else:
        session.close()
        return 'Car not found'


@app.delete('/cars/{id}', tags=['Cars'])
def delete_car(id: int):
    session = Session()
    session.query(Car).filter_by(id=id).delete()
    session.commit()
    session.close()
    return 'Car deleted successfully'


# pydantic class for user
class Usertype(BaseModel):
    name: str
    email: str


# code to handle users
@app.get('/users', tags=['Users'])
def get_users():
    session = Session()
    users = session.query(User).all()
    return users


@app.post('/users/{id}', tags=['Users'])
def add_user(user: Usertype):
    session = Session()
    user1 = User(name=user.name, email=user.email)
    session.add(user1)
    session.commit()
    session.close()
    return 'User added successfully'


# pydantic class for reviews
class Reviewtype(BaseModel):
    name: str
    email: str


# code to handle reviews
@app.get('/users', tags=['Users'])
def get_users():
    session = Session()
    users = session.query(User).all()
    return users


@app.post('/users/{id}', tags=['Users'])
def add_user(user: Usertype):
    session = Session()
    user1 = User(name=user.name, email=user.email)
    session.add(user1)
    session.commit()
    session.close()
    return 'User added successfully'
