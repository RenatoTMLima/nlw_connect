import pytest
from .eventos_link_repository import EventosLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_eventos():
    event_id = 2
    subscriber_id = 2
    repo = EventosLinkRepository()

    repo.insert(event_id=event_id, subscriber_id=subscriber_id)
