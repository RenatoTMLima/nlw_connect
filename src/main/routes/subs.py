from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscriber_creator_validator import subscriber_creator_validator
from src.model.repositories.subscribers_repository import SubscribersRepository
from src.controllers.subscribers.subscriber_creator import SubscriberCreator
from src.controllers.subscribers.subscriber_manager import SubscriberManager

subs_route_bp = Blueprint("subscriber_route", __name__)


@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_sub():
    subscriber_creator_validator(request)

    http_request = HttpRequest(request.json)

    subs_repo = SubscribersRepository()

    sub_creator = SubscriberCreator(subs_repo)

    http_response = sub_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code


@subs_route_bp.route("/subscriber/link/<link>/event/<event_id>", methods=["GET"])
def subscribers_by_link(link, event_id):
    subs_repo = SubscribersRepository()
    sub_manager = SubscriberManager(subs_repo)

    http_request = HttpRequest(param={"link": link, "event_id": event_id})

    http_response = sub_manager.get_subscribers_by_link(http_request)

    return jsonify(http_response.body), http_response.status_code


@subs_route_bp.route("/subscriber/ranking/event/<event_id>", methods=["GET"])
def link_ranking(event_id):
    subs_repo = SubscribersRepository()
    sub_manager = SubscriberManager(subs_repo)

    http_request = HttpRequest(param={"event_id": event_id})

    http_response = sub_manager.get_event_ranking(http_request)

    return jsonify(http_response.body), http_response.status_code
