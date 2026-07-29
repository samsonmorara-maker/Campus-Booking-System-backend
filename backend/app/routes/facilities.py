"""
Facility routes without Flask Blueprints.

Routes are registered directly on the Flask app.
"""

from flask import jsonify, request
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


def register_facility_routes(app):
    """
    Register facility routes directly on Flask app.
    """


    @app.route("/api/facilities", methods=["GET"])
    def get_facilities():

        facilities = get_all_facilities()

        return jsonify(
            facilities_schema.dump(facilities)
        ), 200


    @app.route(
        "/api/facilities/<int:facility_id>",
        methods=["GET"]
    )
    def get_single_facility(facility_id):

        facility = get_facility_by_id(facility_id)

        if not facility:
            return jsonify({
                "message": "Facility not found"
            }), 404

        return jsonify(
            facility_schema.dump(facility)
        ), 200


    @app.route(
        "/api/facilities/search",
        methods=["GET"]
    )
    def search():

        search_term = request.args.get("q")

        if not search_term:
            return jsonify({
                "message": "Search term is required"
            }), 400

        facilities = search_facilities(search_term)

        return jsonify(
            facilities_schema.dump(facilities)
        ), 200


    @app.route(
        "/api/facilities",
        methods=["POST"]
    )
    def add_facility():

        try:
            data = request.get_json()

            validated_data = facility_schema.load(data)

            facility = create_facility(validated_data)

            return jsonify(
                facility_schema.dump(facility)
            ), 201

        except ValidationError as error:
            return jsonify({
                "errors": error.messages
            }), 400


    @app.route(
        "/api/facilities/<int:facility_id>",
        methods=["PUT"]
    )
    def edit_facility(facility_id):

        facility = get_facility_by_id(facility_id)

        if not facility:
            return jsonify({
                "message": "Facility not found"
            }), 404

        try:
            data = request.get_json()

            validated_data = facility_schema.load(
                data,
                partial=True
            )

            updated_facility = update_facility(
                facility,
                validated_data
            )

            return jsonify(
                facility_schema.dump(updated_facility)
            ), 200

        except ValidationError as error:
            return jsonify({
                "errors": error.messages
            }), 400


    @app.route(
        "/api/facilities/<int:facility_id>",
        methods=["DELETE"]
    )
    def remove_facility(facility_id):

        facility = get_facility_by_id(facility_id)

        if not facility:
            return jsonify({
                "message": "Facility not found"
            }), 404

        delete_facility(facility)

        return jsonify({
            "message": "Facility deleted successfully"
        }), 200