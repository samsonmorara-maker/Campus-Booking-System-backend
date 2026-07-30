"""
Facility schema.

Handles validation of facility input
and converts Facility objects into JSON.
"""

from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validates,
)


class FacilitySchema(Schema):
    """
    Schema for Facility validation
    and serialization.
    """

    id = fields.Int(
        dump_only=True
    )

    name = fields.Str(
        required=True
    )

    category = fields.Str(
        required=True
    )

    location = fields.Str(
        required=True
    )

    capacity = fields.Int(
        required=True
    )

    description = fields.Str(
        allow_none=True
    )

    image = fields.Str(
        allow_none=True
    )

    available = fields.Bool(
        load_default=True
    )

    created_at = fields.DateTime(
        dump_only=True
    )


    @validates("name")
    def validate_name(self, value, **kwargs):
        """
        Ensure facility name is not empty.
        """

        if not value or not value.strip():
            raise ValidationError(
                "Facility name cannot be empty."
            )


    @validates("category")
    def validate_category(self, value, **kwargs):
        """
        Ensure category is not empty.
        """

        if not value or not value.strip():
            raise ValidationError(
                "Category cannot be empty."
            )


    @validates("location")
    def validate_location(self, value, **kwargs):
        """
        Ensure location is not empty.
        """

        if not value or not value.strip():
            raise ValidationError(
                "Location cannot be empty."
            )


    @validates("capacity")
    def validate_capacity(self, value, **kwargs):
        """
        Ensure capacity is positive.
        """

        if value <= 0:
            raise ValidationError(
                "Capacity must be greater than zero."
            )


facility_schema = FacilitySchema()

facilities_schema = FacilitySchema(
    many=True
)