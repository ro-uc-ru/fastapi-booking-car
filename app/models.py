from pydantic import BaseModel
from datetime import date
from typing import List


#definimos la clase acorde al tipo de dato de nuestro cars.json
class Car(BaseModel):
    id: int
    brand: str
    model: str
    booked_dates: List[str] | None


#classe para hacer las requests y hacer booking del coche
class BookCar(BaseModel):
    id: int
    date: date


