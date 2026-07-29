def booking_to_dict(booking):
    return {
        "id": booking.id,
        "user_id": booking.user_id,
        "facility_id": booking.facility_id,
        "booking_date": str(booking.booking_date),
        "start_time": str(booking.start_time),
        "end_time": str(booking.end_time),
        "status": booking.status,
    }
