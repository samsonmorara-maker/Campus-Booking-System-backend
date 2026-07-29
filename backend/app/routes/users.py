from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user import UserService


def register_user_routes(app):

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

        response, status = UserService.update_profile(
            user_id,
            data,
        )

        return jsonify(response), status