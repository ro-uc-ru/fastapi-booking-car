# FastAPI Booking Car

API REST para reservar coches utilizando FastAPI, con persistencia en JSON y manejo de logs.

---

## Descripción

Esta API permite:
- Consultar coches disponibles para la fecha actual.
- Reservar un coche para un día específico.
- Maneja los bookings evitando solapamientos.
- Los logs se escriben en app.log a medida que se hacen peticiones.

El backend está construido con FastAPI y la base de datos es un archivo JSON simple.

---

## Diseño

La aplicación está diseñada para leer un json con un formato específico y, con ese json de coches, hacer requests para poder:
- Ver los coches disponibles en ese dia.
- Hacer un booking de un coche para un dia concreto

La aplicación está modularizada de tal forma que tanto las requests como las funciones que cargan y modifican el json se encuentran separadas del fichero main, así mismo, la descripción del logger también se encuentra en otro fichero.

```text
ARQUITECTURA                                 ESTRUCTURA

+-------------------+                        ├── app
|  Cliente (curl,   |                        │   ├── __init__.py
|  navegador, etc.) |                        │   ├── main.py   
+---------+---------+                        │   ├── db_connector.py 
          |                                  │   ├── logger.py   
          v                                  │   └── models.py                               
+-------------------+                        │ 
|     FastAPI App   |                        ├── cars.json   
|    (app.main)     |                        ├── app.log  
+---------+---------+                        ├── test.py   
          |                                  ├── requirements.txt 
          v                                  ├── Dockerfile  
+-------------------+
|   db_connector.py |
| (manejo de JSON)  |
+---------+---------+
          |
          v
+-------------------+
|     cars.json     |
|  (base de datos)  |
+-------------------+

```
---

## Requerimientos

- Es necesario estar trabajando en un entorno virtual de tal forma que hay que instalar las dependencias usando el requirements.txt

```bash
pip install -r requirements.txt
```
- Es necesario disponer de Docker desktop o similares para poder construir la imagen con el Dockerfile.


---

## Test

Los tests que hay disponibles son:
 - Checkear que la app está funcionando correctamente
 - Checkear una reserva exitosa

Para poder correr los test, se debe correr el siguiente comando:

```bash
pytest test.py
```
En ese momento, en la terminal se visualiza si se han pasado los tests correctamente, incluso es posible ver los logs de los tests en app.log.


## Uso de la aplicación
- En caso que se use en local, sin tener en cuenta Docker:
  ```bash
  python app/main.py #en caso de que main.py contenga uvicorn.run(app)
  ```
  o bien
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000
  ```
- En caso de usar Docker:
  ```bash
  docker build -t fastapi-app .
  docker run -p 8000:8000 fastapi-app 
  ```
- Finalmente probamos la app con una petición:
  ```curl
  curl -X GET http://localhost:8000/get-cars
  ```

