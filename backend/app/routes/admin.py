from flask import jsonify, request
from app import app
from app.services import admin as admin_service
from app.services import dashboard as dashboard_service
from app.schemas.booking import booking_to_dict
from app.schemas.user import user_to_dict
from app.utils.decorators import admin_required

@app.route("/api/admin/dashboard/stats", methods=["GET"])
@admin_required()
def dashboard_stats():
    return jsonify(dashboard_service.get_dashboard_stats()), 200

@app.route("/api/admin/bookings", methods=["GET"])
@admin_required()
def list_bookings():
    status = request.args.get("status")
    bookings = admin_service.get_all_bookings(status)
    return jsonify([booking_to_dict(b) for b in bookings]), 200

@app.route("/api/admin/bookings/<int:booking_id>/approve", methods=["PATCH"])
@admin_required()
def approve_booking_route(booking_id):
    booking, error = admin_service.approve_booking(booking_id)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(booking_to_dict(booking)), 200

@app.route("/api/admin/bookings/<int:booking_id>/reject", methods=["PATCH"])
@admin_required()
def reject_booking_route(booking_id):
    booking, error = admin_service.reject_booking(booking_id)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(booking_to_dict(booking)), 200

@app.route("/api/admin/users", methods=["GET"])
@admin_required()
def list_users():
    users = admin_service.get_all_users()
    return jsonify([user_to_dict(u) for u in users]), 200
