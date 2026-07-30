from flask import jsonify, request
from app import app
from app.services.auth import AuthService

@app.route("/api/auth/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "message": "Request body is required."
        }), 400
    response, status = AuthService.register(data)
    return jsonify(response), status

@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "message": "Request body is required."
        }), 400
    response, status = AuthService.login(data)
    return jsonify(response), status