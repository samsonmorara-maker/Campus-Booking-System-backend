from flask import request
from app import app
from app.schemas.schedule import schedules_schema
from app.services.schedule import (get_all_schedules, filter_schedules)


# Get all class schedules
@app.route("/schedules", methods=["GET"])
def get_schedules():
    schedules = get_all_schedules()
    return schedules_schema.jsonify(schedules), 200

# Filter schedules by day and/or facility
@app.route("/schedules/filter", methods=["GET"])
def get_filtered_schedules():
    day = request.args.get("day")
    facility_id = request.args.get(
        "facility_id",
        type=int
    )
    schedules = filter_schedules(
        day=day,
        facility_id=facility_id
    )


    return schedules_schema.jsonify(schedules), 200