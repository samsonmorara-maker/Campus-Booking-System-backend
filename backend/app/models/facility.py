from app.extensions import db

class Facility(db.Model):
    __tablename__ = "facilities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(120))
    capacity = db.Column(db.Integer)
    image = db.Column(db.String(255))  # URL string
    available = db.Column(db.Boolean, default=True)

    bookings = db.relationship("Booking", backref="facility", lazy=True)