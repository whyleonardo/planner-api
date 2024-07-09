import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
LINK_ID = str(uuid.uuid4())
TRIP_ID = str(uuid.uuid4())
LINK = "https://airbnb.com"
TITLE = "Airbnb"


@pytest.mark.skip(reason="Interaction with database")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    link_infos = {"id": LINK_ID, "trip_id": TRIP_ID, "link": LINK, "title": TITLE}

    links_repository.registry_link(link_infos)


@pytest.mark.skip(reason="Interaction with database")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_repository.find_links_from_trip(TRIP_ID)
