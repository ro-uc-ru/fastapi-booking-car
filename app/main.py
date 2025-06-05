from fastapi import FastAPI, HTTPException
from .db_connector import load_db, save_booking
from datetime import date
from .models import Car, BookCar
from .logger import logger

#inicializamos tanto la API como el logger
app = FastAPI()
logger.info("Starting API...")


#el root path, simplemente hacemos saber que funciona
@app.get('/')
def root():
    logger.info("request to root")
    return {"status": 200 }


@app.get('/get-cars')
def get_cars() -> list[Car]:
    logger.info("Request to see availabe cars")
    #pasamos la fecha de hoy en isoformat para visualizar los coches disponibles para hoy
    today: str = date.today().isoformat()
    cars = load_db()
    available_cars: list[Car] = [car for car in cars if today not in car.get('booked_dates')]
    return available_cars


@app.post('/book-car')
def book_car(request: BookCar):
    logger.info("Request to book a car")
    #comprobamos si se puede hacer booking del coche 
    is_booked: bool = save_booking(request = request)
    if not is_booked:
        #En caso que ya esté booked, lo hacemos saber
        logger.error("Failed to book car, the car is already booked for this day")
        raise HTTPException(status_code = 400, detail= "Car not available for booking")
    
    #hacemos saber al usuario que el coche que queria hacer booking, ha sido booked exitosamente
    logger.info("Car booked succesfully")
    return {"status": f"Car with id {request.id} has been booked for {request.date}"}
        



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port = 8080)
