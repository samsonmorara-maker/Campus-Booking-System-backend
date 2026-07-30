from flask import request, jsonify
from app import app
from app.schemas.booking import (booking_schema, bookings_schema)
from app.services.booking import (create_booking, get_user_bookings, cancel_booking, check_availability)


# Create a booking
@app.route("/bookings", methods=["POST"])
def create_booking_route():
    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Booking data is required."
        }), 400

    booking = create_booking(data)

    if booking is None:
        return jsonify({
            "message": "Facility is not available for the selected time."
        }), 400


    return booking_schema.jsonify(booking), 201

# Get all bookings for a user
@app.route("/bookings/<int:user_id>", methods=["GET"])
def get_bookings(user_id):
    bookings = get_user_bookings(user_id)

    return bookings_schema.jsonify(bookings), 200

# Cancel a booking
@app.route("/bookings/<int:booking_id>/cancel", methods=["PATCH"])
def cancel_booking_route(booking_id):
    booking = cancel_booking(booking_id)

    if booking is None:
        return jsonify({
            "message": "Booking not found."
        }), 404

    if booking is False:
        return jsonify({
            "message": "Only pending bookings can be cancelled."
        }), 400


    return booking_schema.jsonify(booking), 200

@app.route("/bookings/availability", methods=["GET"])
def check_availability_route():
    facility_id = request.args.get(
        "facility_id",
        type=int
    )
    booking_date = request.args.get(
        "booking_date"
    )
    start_time = request.args.get(
        "start_time"
    )
    end_time = request.args.get(
        "end_time"
    )
    available = check_availability(
        facility_id,
        booking_date,
        start_time,
        end_time
    )
    return jsonify({
        "available": available
    }), 200