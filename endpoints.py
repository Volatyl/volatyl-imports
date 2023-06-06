from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from models import Car, engine, User, Review, user_car
from typing import Optional, List

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


class Cartype2(BaseModel):
    brand: Optional[str] = None
    model: Optional[str]
    year: Optional[int] = None
    mileage: Optional[int]
    price: Optional[int]
    cc: Optional[int]
    description: Optional[str]


@app.patch('/cars/update/{id}', tags=['Cars'])
def edit_car(id: int, car: Cartype2):
    session = Session()
    car1 = session.query(Car).filter_by(id=id).first()
    if car1:
        for attr, value in car.dict(exclude_unset=True).items():
            setattr(car1, attr, value)

        session.commit()
        # session.close()
        return 'Car updated successfully'
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
    review: str
    user_id: int
    car_id: int


# code to handle reviews
@app.get('/reviews', tags=['Reviews'])
def get_review():
    session = Session()
    reviews = session.query(Review).all()
    return reviews


@app.post('/reviews/{id}', tags=['Reviews'])
def add_review(review: Reviewtype):
    session = Session()
    review1 = Review(review=review.review,
                     user_id=review.user_id, car_id=review.car_id)
    session.add(review1)
    session.commit()
    session.close()
    return 'Review added successfully'


@app.delete('/reviews/{id}', tags=['Reviews'])
def delete_review(id: int):
    session = Session()
    session.query(Review).filter_by(id=id).delete()
    session.commit()
    session.close()
    return 'Review deleted successfully'

# pydantic code for relationship


class Car_user(BaseModel):
    user_id = int
    car_id = int

# code to add user & car relationship


@app.post('/', tags=['relationship'])
def add_rel(details: Car_user):
    session = Session()
    car = session.query(Car).filter_by(id=details.car_id).first()
    user = session.query(User).filter_by(id=details.user_id).first()

    car.users.append(user)
    session.commit()
    session.commit()
    session.close()
