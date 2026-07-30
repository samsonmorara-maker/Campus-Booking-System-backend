from app.models.booking import Booking
from app.models.facility import Facility
from app.utils.statistics import calculate_percentage

def get_dashboard_stats():
    total_facilities = Facility.query.count()
    total_bookings = Booking.query.count()
    pending = Booking.query.filter_by(status="pending").count()
    approved = Booking.query.filter_by(status="approved").count()
    rejected = Booking.query.filter_by(status="rejected").count()

    return {
        "total_facilities": total_facilities,
        "total_bookings": total_bookings,
        "pending_bookings": pending,
        "approved_bookings": approved,
        "rejected_bookings": rejected,
        "approval_rate": calculate_percentage(approved, total_bookings),
    }
