"""
Facility routes.

This file contains REST API endpoints
for facility management.
"""

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.schemas.facility import (
    facilities_schema,
    facility_schema,
)

from app.services.facility import (
    get_all_facilities,
    get_facility_by_id,
    search_facilities,
    create_facility,
    update_facility,
    delete_facility,
)


# Create Blueprint
facility_bp = Blueprint(
    "facilities",
    __name__,
    url_prefix="/api/facilities"
)


@facility_bp.route("", methods=["GET"])
def get_facilities():
    """Get all facilities."""
    facilities = get_all_facilities()
    return jsonify(facilities_schema.dump(facilities)), 200


@facility_bp.route("/<int:facility_id>", methods=["GET"])
def get_single_facility(facility_id):
    """Get one facility by ID."""
    facility = get_facility_by_id(facility_id)

    if not facility:
        return jsonify({"message": "Facility not found"}), 404

    return jsonify(facility_schema.dump(facility)), 200


@facility_bp.route("/search", methods=["GET"])
def search():
    """Search facilities by name, category, or location."""
    search_term = request.args.get("q", "").strip()

    if not search_term:
        return jsonify({"message": "Search term is required"}), 400

    facilities = search_facilities(search_term)
    return jsonify(facilities_schema.dump(facilities)), 200


@facility_bp.route("", methods=["POST"])
def add_facility():
    """Create a new facility."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"message": "A JSON request body is required"}), 400

    try:
        facility = create_facility(facility_schema.load(data))
    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    return jsonify(facility_schema.dump(facility)), 201


@facility_bp.route("/<int:facility_id>", methods=["PUT"])
def edit_facility(facility_id):
    """Update an existing facility."""
    facility = get_facility_by_id(facility_id)

    if not facility:
        return jsonify({"message": "Facility not found"}), 404

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"message": "A JSON request body is required"}), 400

    try:
        updated_facility = update_facility(
            facility, facility_schema.load(data, partial=True)
        )
    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    return jsonify(facility_schema.dump(updated_facility)), 200


@facility_bp.route("/<int:facility_id>", methods=["DELETE"])
def remove_facility(facility_id):
    """Delete a facility."""
    facility = get_facility_by_id(facility_id)

    if not facility:
        return jsonify({"message": "Facility not found"}), 404

    delete_facility(facility)
    return jsonify({"message": "Facility deleted successfully"}), 200
