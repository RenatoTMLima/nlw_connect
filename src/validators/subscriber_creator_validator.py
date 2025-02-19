from cerberus import Validator

def subscriber_creator_validator(request: any):
    body_validator = Validator({
        "name": {
            "type": "string",
            "required": True,
            "empty": False
        },
        "email": {
            "type": "string",
            "required": True,
            "empty": False
        },
        "link": {
            "type": "string",
            "required": False,
            "empty": False
        },
        "event_id": {
            "type": "integer",
            "required": True,
            "empty": False
        }
    })
    response = body_validator.validate(request.json)

    if response is False:
        print(body_validator.errors)