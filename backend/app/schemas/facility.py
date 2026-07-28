"""
Facility schema.

This file validates facility data received from the client
and serializes Facility objects into JSON responses.
"""

from marshmallow import Schema, ValidationError, fields, validates


class FacilitySchema(Schema):
    """Schema for serializing and validating facility data."""

    id = fields.Int(dump_only=True)

    name = fields.Str(required=True)

    category = fields.Str(required=True)

    location = fields.Str(required=True)

    capacity = fields.Int(required=True)

    description = fields.Str(allow_none=True)

    image = fields.Str(allow_none=True)

    available = fields.Bool()

    created_at = fields.DateTime(dump_only=True)

    @validates("capacity")
    def validate_capacity(self, value):
        """
        Ensure facility capacity is greater than zero.
        """
        if value <= 0:
            raise ValidationError(
                "Capacity must be greater than zero."
            )


# Schema for a single facility
facility_schema = FacilitySchema()

# Schema for multiple facilities
facilities_schema = FacilitySchema(many=True)