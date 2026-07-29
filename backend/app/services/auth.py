import re
from flask_jwt_extended import create_access_token
from app.extensions import db
from app.models.user import User
from app.schemas.user import user_schema
from app.utils.password import hash_password, check_password

class AuthService:
    @staticmethod
    def register(data):
        required_fields = [
            "first_name",
            "last_name",
            "email",
            "password",
        ]
        for field in required_fields:
            if not data.get(field):
                return {
                    "message": f"{field} is required."
                }, 400
        email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
        if not re.match(email_pattern, data["email"]):
            return {
                "message": "Invalid email address."
            }, 400
        if len(data["password"]) < 8:
            return {
                "message": "Password must be at least 8 characters long."
            }, 400
        existing_user = User.query.filter_by(
            email=data["email"]
        ).first()
        if existing_user:
            return {
                "message": "Email already exists."
            }, 409
        new_user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            password=hash_password(data["password"]),
            role="student",
        )
        db.session.add(new_user)
        db.session.commit()
        return {
            "message": "Registration successful.",
            "user": user_schema.dump(new_user),
        }, 201

    @staticmethod
    def login(data):
        if not data.get("email") or not data.get("password"):
            return {
                "message": "Email and password are required."
            }, 400
        user = User.query.filter_by(
            email=data["email"]
        ).first()
        if not user:
            return {
                "message": "Invalid email or password."
            }, 401
        if not check_password(
            data["password"],
            user.password,
        ):
            return {
                "message": "Invalid email or password."
            }, 401
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "role": user.role
            },
        )
        return {
            "message": "Login successful.",
            "access_token": access_token,
            "user": user_schema.dump(user),
        }, 200