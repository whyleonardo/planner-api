import pytest
import uuid
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

from datetime import datetime, timedelta


db_connection_handler.connect()
trip_id = str(uuid.uuid4)


@pytest.mark.skip(reason="interaction with database")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_infos = {
        "id": trip_id,
        "destination": "Gramado",
        "start_date": datetime.strptime("12-08-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("12-08-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Christian Leonardo",
        "owner_email": "christian.lsb16@gmail.com",
    }

    trips_repository.create_trip(trips_infos)


@pytest.mark.skip(reason="interaction with database")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.find_trip_by_id(trip_id)


@pytest.mark.skip(reason="interaction with database")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.update_trip_status(trip_id)
