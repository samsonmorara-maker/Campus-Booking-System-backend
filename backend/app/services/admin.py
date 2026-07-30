from app.extensions import db
from app.models.booking import Booking
from app.models.user import User

def get_all_bookings(status=None):
    query = Booking.query
    if status:
        query = query.filter_by(status=status)
    return query.all()

def approve_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.status.lower() != "pending":
        return None, "Booking is not pending"
    booking.status = "approved"
    db.session.commit()
    return booking, None

def reject_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.status.lower() != "pending":
        return None, "Booking is not pending"
    booking.status = "rejected"
    db.session.commit()
    return booking, None

def get_all_users():
    return User.query.all()
