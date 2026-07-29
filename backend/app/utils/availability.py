from app.models.booking import Booking
from app.extensions import db


def check_availability(
    facility_id,
    booking_date,
    start_time,
    end_time
):

    conflicting_booking = Booking.query.filter(
        Booking.facility_id == facility_id,
        Booking.booking_date == booking_date,
        Booking.status.in_(
            ["Pending", "Approved"]
        ),
        Booking.start_time < end_time,
        Booking.end_time > start_time
    ).first()


    if conflicting_booking:
        return False

    return True