from app.extensions import ma
from app.models.class_schedule import ClassSchedule


class ClassScheduleSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ClassSchedule
        load_instance = True
        include_fk = True


schedule_schema = ClassScheduleSchema()

schedules_schema = ClassScheduleSchema(many=True)