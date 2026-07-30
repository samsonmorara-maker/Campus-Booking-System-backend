from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token
from app.extensions import db
from app.models.user import User
from app.schemas.user import user_schema
from app.utils.password import hash_password, check_password

class AuthService:
    @staticmethod
    def register(data):
        required_fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )
        for field in required_fields:
            if not data.get(field):
                return {
                    "message": f"{field.replace('_', ' ').title()} is required."
                }, 400
        email = data["email"].strip().lower()
        existing_user = User.query.filter_by(
            email=email
        ).first()
        if existing_user:
            return {
                "message": "Email already exists."
            }, 409
        try:
            new_user = User(
                first_name=data["first_name"].strip(),
                last_name=data["last_name"].strip(),
                email=email,
                password=hash_password(data["password"]),
                role=User.STUDENT,
            )
            db.session.add(new_user)
            db.session.commit()
            return {
                "message": "Registration successful.",
                "user": user_schema.dump(new_user),
            }, 201
        except SQLAlchemyError:
            db.session.rollback()
            return {
                "message": "Unable to register user."
            }, 500

    @staticmethod
    def login(data):
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")
        if not email or not password:
            return {
                "message": "Email and password are required."
            }, 400
        user = User.query.filter_by(
            email=email
        ).first()
        if not user:
            return {
                "message": "Invalid email or password."
            }, 401
        if not check_password(
            password,
            user.password,
        ):
            return {
                "message": "Invalid email or password."
            }, 401
        access_token = create_access_token(
            identity=user.id,
            additional_claims={
                "role": user.role
            },
        )
        return {
            "message": "Login successful.",
            "access_token": access_token,
            "user": user_schema.dump(user),
        }, 200