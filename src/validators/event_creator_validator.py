from cerberus import Validator

def events_creator_validator(request: any):
    body_validator = Validator({
        "name": {
            "type": "string",
            "required": True,
            "empty": False
        }
    })
    response = body_validator.validate(request.json)

    if response is False:
        raise Exception(body_validator.errors)