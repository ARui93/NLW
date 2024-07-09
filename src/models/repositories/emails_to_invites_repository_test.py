import pytest
import uuid
from src.models.settings.db_connection_handler import db_connetion_handler
from .emails_to_invites_repository import EmailsToRepository

db_connetion_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interação com o banco")
def test_registry_email():
    conn = db_connetion_handler.get_connection()
    emails_to_invite_repository = EmailsToRepository(conn)
    
    email_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olamundo@email.com"
    }

    emails_to_invite_repository.registry_email(email_trips_infos)

@pytest.mark.skip(reason="Interação com o banco")
def test_find_email_from_trip():
    conn = db_connetion_handler.get_connection()
    emails_to_invite_repository = EmailsToRepository(conn)

    emails = emails_to_invite_repository.find_email_from_trip(trip_id)
    print()
    print(emails)