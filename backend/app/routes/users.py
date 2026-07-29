from flask import jsonify, request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
)
from app.main import app
from app.services.user import UserService

@app.route("/api/users/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    response, status = UserService.get_profile(user_id)
    return jsonify(response), status

@app.route("/api/users/profile", methods=["PUT"])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    if not data:
        return jsonify({
            "message": "Request body is required."
        }), 400
    response, status = UserService.update_profile(
        user_id,
        data,
    )
    return jsonify(response), status