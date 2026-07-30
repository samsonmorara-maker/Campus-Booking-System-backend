from datetime import datetime
from app.extensions import db


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column( db.Integer, db.ForeignKey("users.id"), nullable=False)

    facility_id = db.Column(db.Integer, db.ForeignKey("facilities.id"), nullable=False)

    booking_date = db.Column(db.Date, nullable=False)

    start_time = db.Column(db.Time, nullable=False)

    end_time = db.Column(db.Time, nullable=False)

    status = db.Column(db.String(20), nullable=False, default="pending")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="bookings")

    facility = db.relationship("Facility", back_populates="bookings")

    def __repr__(self):
        return f"<Booking {self.id}>"
