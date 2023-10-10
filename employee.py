import dbFun
import pandas as pd

import enum_values


def track():
    # {1: (3, 12, 'LOWPOWER', 2),
    # 2: (3, 12, 'LOWPOWER', 2),
    # 3: (3, 12, 'LOWPOWER', 2),
    # 4: (2, 18, 'VACANT', 2)}
    data = dbFun.get_latest_vehicleInfos()
    result = {}
    for item in data.items():
        series = pd.Series(item[1], index=['info_id', 'time', 'status', 'location_id'])

        location = dbFun.get_loc_name(series['location_id'])
        series['station_name'] = location[0][0]
        series['postcode'] = location[0][1]
        series = series.drop("location_id")

        result[item[0]] = series
    return result


def charge(vehicle_id, time, location_id):
    status = dbFun.check_status(vehicle_id)

    if status == enum_values.Status.LOWPOWER.value:
        status = enum_values.Status.VACANT.value
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

        return True
    else:
        return False


def repair(vehicle_id, time, location_id):
    status = dbFun.check_status(vehicle_id)

    if status == enum_values.Status.BROKEN.value:
        status = enum_values.Status.VACANT.value
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

        return True
    else:
        return False


def move(vehicle_id, time, location_id):
    status = enum_values.Status.VACANT.value
    # create new vehicleInfo, add it to the table
    dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)
