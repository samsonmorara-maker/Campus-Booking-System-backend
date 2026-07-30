from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from app.models.user import User
from app.schemas.user import user_schema
from app.utils.password import hash_password

class UserService:
    @staticmethod
    def get_profile(user_id):
        user = db.session.get(User, user_id)
        if not user:
            return {
                "message": "User not found."
            }, 404
        return {
            "user": user_schema.dump(user)
        }, 200

    @staticmethod
    def update_profile(user_id, data):
        user = db.session.get(User, user_id)
        if not user:
            return {
                "message": "User not found."
            }, 404
        try:
            if "first_name" in data and data["first_name"].strip():
                user.first_name = data["first_name"].strip()
            if "last_name" in data and data["last_name"].strip():
                user.last_name = data["last_name"].strip()
            if "email" in data and data["email"].strip():
                email = data["email"].strip().lower()
                existing_user = User.query.filter_by(
                    email=email
                ).first()
                if existing_user and existing_user.id != user.id:
                    return {
                        "message": "Email already exists."
                    }, 409
                user.email = email
            if "password" in data and data["password"]:
                user.password = hash_password(data["password"])
            db.session.commit()
            return {
                "message": "Profile updated successfully.",
                "user": user_schema.dump(user),
            }, 200
        except SQLAlchemyError:
            db.session.rollback()
            return {
                "message": "Unable to update profile."
            }, 500