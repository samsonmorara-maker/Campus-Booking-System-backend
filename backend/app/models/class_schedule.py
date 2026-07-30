from app.extensions import db


class ClassSchedule(db.Model):
    __tablename__ = "class_schedules"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    facility_id = db.Column(
        db.Integer,
        db.ForeignKey("facilities.id"),
        nullable=False
    )

    course_name = db.Column(
        db.String(100),
        nullable=False
    )

    lecturer = db.Column(
        db.String(100),
        nullable=False
    )

    day = db.Column(
        db.String(20),
        nullable=False
    )

    start_time = db.Column(
        db.Time,
        nullable=False
    )

    end_time = db.Column(
        db.Time,
        nullable=False
    )

    semester = db.Column(
        db.String(30),
        nullable=False
    )

    facility = db.relationship(
        "Facility",
        back_populates="class_schedules"
    )

    def __repr__(self):
        return f"<ClassSchedule {self.course_name}>"