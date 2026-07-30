from app.extensions import ma
from app.models.booking import Booking


class BookingSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Booking
        load_instance = True
        include_fk = True


booking_schema = BookingSchema()

bookings_schema = BookingSchema(many=True)


def booking_to_dict(booking):
    """Serialize a booking for the admin endpoints."""
    return {
        "id": booking.id,
        "user_id": booking.user_id,
        "facility_id": booking.facility_id,
        "booking_date": str(booking.booking_date),
        "start_time": str(booking.start_time),
        "end_time": str(booking.end_time),
        "status": booking.status,
    }
