from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscriberCreator:
    def __init__(self, events_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = events_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body
        subscriber_email = subscriber_info["email"]
        event_id = subscriber_info["event_id"]

        self.__check_sub(subscriber_email, event_id)
        self.__insert_sub(subscriber_info)
        return self.__format_response(subscriber_info)

    def __check_sub(self, subscriber_email: str, event_id: int) -> None:
        response = self.__subscribers_repo.select_subscriber(subscriber_email, event_id)

        if response: raise Exception("Subscriber already exists!")

    def __insert_sub(self, subscriber_info: dict) -> None:
        self.__subscribers_repo.insert(subscriber_info)

    def __format_response(self, subscriber_info: dict) -> HttpResponse:
        return HttpResponse(
            {
                "Type": "Subscriber",
                "count": 1,
                "attributes": subscriber_info
            },
            201
        )