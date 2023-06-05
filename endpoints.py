from fastapi import FastAPI
from models import Car, Brand, engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

Session = sessionmaker(bind=engine)
session = Session()


@app.get('/', tags=['home'])
def get_data():
    with session as s:
        cars = s.query(Car).all()
    return cars

@app.post('/')
def add_brand():
    with session as s:
        brand
