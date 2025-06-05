from .app.main import app
from fastapi.testclient import TestClient
from unittest.mock import patch


client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"status": 200 }



#testeamos una reserva exitosa
@patch("app.main.save_booking")
def test_ok_booking(mock_save_booking):
    mock_save_booking.return_value =  True
    #probamos con este ejemplo
    payload = {"id": 1, "date": "2025-06-05"}
    response = client.post('/book-car', json = payload)
    assert response.status_code == 200
    assert response.json() == {"status": f"Car with id {payload['id']} has been booked for {payload['date']}"}


#testeamos una reserva fallida
@patch("app.main.save_booking")
def test_bad_booking(mock_save_booking):
    mock_save_booking.return_value =  False
    #probamos con este ejemplo, la idea es que sea un booking incorrecto
    payload = {"id": 1, "date": "2025-06-05"}
    response = client.post('/book-car', json = payload)
    assert response.status_code == 400
    assert response.json() == {"detail": "Car not available for booking"}