from flask import request, jsonify
from app.services.auth import AuthService


def register_auth_routes(app):

    @app.route("/api/auth/register", methods=["POST"])
    def register():
        data = request.get_json()

        if not data:
            return jsonify({
                "message": "Request body is required."
            }), 400

        response, status = AuthService.register(data)
        return jsonify(response), status

    @app.route("/api/auth/login", methods=["POST"])
    def login():
        data = request.get_json()

        if not data:
            return jsonify({
                "message": "Request body is required."
            }), 400

        response, status = AuthService.login(data)
        return jsonify(response), status