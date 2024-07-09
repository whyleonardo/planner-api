import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
EMAIL_ID = str(uuid.uuid4())
TRIP_ID = str(uuid.uuid4())


@pytest.mark.skip(reason="Interaction with database")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trips_infos = {
        "id": EMAIL_ID,
        "trip_id": TRIP_ID,
        "email": "christian.lsb16@gmail.com",
    }

    emails_to_invite_repository.registry_email(email_trips_infos)


@pytest.mark.skip(reason="Interaction with database")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_from_trip(TRIP_ID)

    print()
    print(emails)
