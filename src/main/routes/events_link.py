from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.event_creator_validator import events_creator_validator
from src.controllers.events_link.events_link_creator import EventsLinkCreator
from src.model.repositories.eventos_link_repository import EventosLinkRepository

event_link_route_bp = Blueprint("event_link_route", __name__)


@event_link_route_bp.route("/events_link", methods=["POST"])
def create_new_event_link():
    http_request = HttpRequest(request.json)

    eventos_link_repo = EventosLinkRepository()

    events__link_creator = EventsLinkCreator(eventos_link_repo)

    http_response = events__link_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code
