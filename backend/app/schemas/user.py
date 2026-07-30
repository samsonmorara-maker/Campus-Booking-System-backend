from app.extensions import ma
from app.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
    password = ma.auto_field(load_only=True)
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)


def user_to_dict(user):
    """Serialize a user without exposing their password."""
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "role": user.role,
    }
