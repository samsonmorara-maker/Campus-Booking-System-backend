from app.models.class_schedule import ClassSchedule


def get_all_schedules():
    return ClassSchedule.query.all()

def get_schedules_by_day(day):
    return ClassSchedule.query.filter_by(
        day=day
    ).all()

def get_schedules_by_facility(facility_id):
    return ClassSchedule.query.filter_by(
        facility_id=facility_id
    ).all()

def filter_schedules(day=None, facility_id=None):
    query = ClassSchedule.query
    if day:
        query = query.filter_by(
            day=day
        )
    if facility_id:
        query = query.filter_by(
            facility_id=facility_id
        )

    return query.all()