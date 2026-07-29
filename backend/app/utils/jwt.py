from app.extensions import jwt

@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    return {
        "message": "Token has expired."
    }, 401

@jwt.invalid_token_loader
def invalid_token(error):
    return {
        "message": "Invalid token."
    }, 401

@jwt.unauthorized_loader
def missing_token(error):
    return {
        "message": "Authorization token is missing."
    }, 401