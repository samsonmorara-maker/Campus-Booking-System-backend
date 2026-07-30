from marshmallow import validate
from app.extensions import ma
from app.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    Marshmallow schema for serializing and deserializing User objects.
    """
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        ordered = True
    first_name = ma.auto_field(
        required=True,
        validate=validate.Length(
            min=2,
            max=100,
        ),
    )
    last_name = ma.auto_field(
        required=True,
        validate=validate.Length(
            min=2,
            max=100,
        ),
    )
    email = ma.Email(
        required=True,
    )
    password = ma.auto_field(
        required=True,
        load_only=True,
        validate=validate.Length(min=8),
    )
    role = ma.auto_field(
        dump_only=True,
    )
    created_at = ma.auto_field(
        dump_only=True,
    )
    updated_at = ma.auto_field(
        dump_only=True,
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)