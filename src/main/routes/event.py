from flask import Blueprint, jsonify, request
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from src.validators.event_creator_validator import events_creator_validator

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    events_creator_validator(request)
    http_request = HttpRequest(request.json)
    print(http_request.body)
    
    http_response = HttpResponse({"estou": "aqui"}, 201)

    return jsonify(http_response.body), http_response.status_code