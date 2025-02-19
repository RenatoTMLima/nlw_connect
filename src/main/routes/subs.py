from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscriber_creator_validator import subscriber_creator_validator
from src.controllers.subscribers.subscriber_creator import SubscriberCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

subs_route_bp = Blueprint("subscriber_route", __name__)

@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_sub():
    subscriber_creator_validator(request)

    http_request = HttpRequest(request.json)

    subs_repo = SubscribersRepository()

    sub_creator = SubscriberCreator(subs_repo)

    http_response = sub_creator.create(http_request)
    
    return jsonify(http_response.body), http_response.status_code