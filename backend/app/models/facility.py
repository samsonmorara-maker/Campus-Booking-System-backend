"""
Facility database model.

This file defines the Facility table structure
used by SQLAlchemy to communicate with PostgreSQL.
"""

from datetime import datetime

from app.extensions import db


class Facility(db.Model):
    """
    Represents a campus facility.

    Examples:
    - Library
    - Computer Lab
    - Meeting Room
    - Sports Hall
    """

    __tablename__ = "facilities"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    location = db.Column(
        db.String(100),
        nullable=False
    )

    capacity = db.Column(
        db.Integer,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    image = db.Column(
        db.String(255),
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Facility {self.name}>"