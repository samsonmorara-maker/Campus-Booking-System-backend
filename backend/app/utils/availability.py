from app.models.booking import Booking
from sqlalchemy import and_, or_


def is_facility_available(
    facility_id,
    booking_date,
    start_time,
    end_time
):
    """
    Check if a facility is available for the requested date and time.

    Returns:
        True  -> facility is available
        False -> there is a conflicting booking
    """

    conflicting_booking = Booking.query.filter(
        Booking.facility_id == facility_id,
        Booking.booking_date == booking_date,
        Booking.status.in_(["Pending", "Approved"]),
        or_(
            # New booking starts during an existing booking
            and_(
                Booking.start_time <= start_time,
                Booking.end_time > start_time
            ),

            # New booking ends during an existing booking
            and_(
                Booking.start_time < end_time,
                Booking.end_time >= end_time
            ),

            # New booking completely covers an existing booking
            and_(
                Booking.start_time >= start_time,
                Booking.end_time <= end_time
            )
        )
    ).first()

    return conflicting_booking is None