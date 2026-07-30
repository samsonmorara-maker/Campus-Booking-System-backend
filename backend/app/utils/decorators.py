from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.user import User


def admin_required():
    """
    Ensure the current authenticated user has the admin role.
    """

    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):

            user_id = get_jwt_identity()
            user = User.query.get(user_id)

            if user is None:
                return jsonify({
                    "message": "User not found."
                }), 404

            if user.role != User.ADMIN:
                return jsonify({
                    "message": "Administrator access required."
                }), 403

            return fn(*args, **kwargs)
        return wrapper

    return decorator