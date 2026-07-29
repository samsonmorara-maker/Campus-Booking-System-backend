from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    bookings = db.relationship(
    "Booking",
    back_populates="user"
     )