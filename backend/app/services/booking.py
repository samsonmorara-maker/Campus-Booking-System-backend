from app.models.booking import Booking
from app.extensions import db


def create_booking(data):

    available = check_availability(
        data["facility_id"],
        data["booking_date"],
        data["start_time"],
        data["end_time"]
    )

    if not available:
        return None


    booking = Booking(
        user_id=data["user_id"],
        facility_id=data["facility_id"],
        booking_date=data["booking_date"],
        start_time=data["start_time"],
        end_time=data["end_time"],
        status="Pending"
    )

    db.session.add(booking)
    db.session.commit()

    return booking

def get_user_bookings(user_id):
    return Booking.query.filter_by(
        user_id=user_id
    ).all()

def cancel_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return None
    if booking.status != "Pending":
        return False

    booking.status = "Cancelled"
    db.session.commit()
    return booking



def check_availability(facility_id, booking_date, start_time, end_time):
    existing_booking = Booking.query.filter(
        Booking.facility_id == facility_id,
        Booking.booking_date == booking_date,
        Booking.status.in_(["Pending", "Approved"]),
        Booking.start_time < end_time,
        Booking.end_time > start_time
    ).first()

    return existing_booking is None