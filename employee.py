import dbFun


def charge(vehicle_id, time, status, location_id):
    # create new vehicleInfo, add it to the table
    dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)


def repair(vehicle_id, time, status, location_id):
    # create new vehicleInfo, add it to the table
    dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)


def move(vehicle_id, time, status, location_id):
    # create new vehicleInfo, add it to the table
    dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)
