from app.extensions import db
from app.models.user import User
from app.schemas.user import user_schema

class UserService:
    @staticmethod
    def get_profile(user_id):
        user = db.session.get(User, user_id)
        if not user:
            return {
                "message": "User not found."
            }, 404
        return user_schema.dump(user), 200

    @staticmethod
    def update_profile(user_id, data):
        user = db.session.get(User, user_id)
        if not user:
            return {
                "message": "User not found."
            }, 404
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        db.session.commit()
        return {
            "message": "Profile updated successfully.",
            "user": user_schema.dump(user)
        }, 200