"""
Facility service.

This file contains all business logic related to
facility management.
"""

from sqlalchemy import or_

from app.extensions import db
from app.models.facility import Facility


def get_all_facilities():
    """
    Return all facilities.
    """
    return Facility.query.order_by(Facility.created_at.desc()).all()


def get_facility_by_id(facility_id):
    """
    Return a single facility by its ID.
    """
    return Facility.query.get(facility_id)


def search_facilities(search_term):
    """
    Search facilities by name, category or location.
    """
    return Facility.query.filter(
        or_(
            Facility.name.ilike(f"%{search_term}%"),
            Facility.category.ilike(f"%{search_term}%"),
            Facility.location.ilike(f"%{search_term}%"),
        )
    ).all()


def create_facility(data):
    """
    Create a new facility.
    """
    facility = Facility(**data)

    db.session.add(facility)
    db.session.commit()

    return facility


def update_facility(facility, data):
    """
    Update an existing facility.
    """
    for key, value in data.items():
        setattr(facility, key, value)

    db.session.commit()

    return facility



def delete_facility(facility):
    """
    Delete a facility only if it has no bookings.
    """
    if facility.bookings:
        return False

    db.session.delete(facility)
    db.session.commit()

    return True