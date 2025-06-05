import json
from .models import BookCar

db = "cars.json"


def load_db():
    with open(db, 'r') as f:
        return json.load(f)
    

#escribimos los cambios si alguien bookea un coche
#devolvemos un bool para el post request
def save_booking(request: BookCar) -> bool:
    cars = load_db()
    update: bool = False
    for car in cars:
        if car.get('id') == request.id:
            #pasamos el formato de la fecha a uno estandar y a str
            booking_date: str = request.date.isoformat()
            if booking_date not in car.get('booked_dates'):
                #comprobamos que la fecha de booking no se encuentre ya en ese coche y si no esta, hacemos update
                car.get('booked_dates').append(booking_date)
                update = True
    
    #reescribimos los cambios en el cars.json
    if update:
        with open(db, 'w') as f:
            json.dump(cars, f, indent = 2)
    
    return update
    





