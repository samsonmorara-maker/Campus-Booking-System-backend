from app.extensions import db


class Facility(db.Model):
    __tablename__ = "facilities"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    bookings = db.relationship(
        "Booking",
        back_populates="facility"
    )

    class_schedules = db.relationship(
        "ClassSchedule",
        back_populates="facility"
    )