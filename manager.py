import pandas as pd
import dbFun


# return a list of series containing all infos of a vehicle
# print(result[0])

# info_id                     1
# time                        1
# status                 RENTED
# station_name    station_name1
# postcode            postcode1
# dtype: object
def report_single(vehicle_id):
    data = dbFun.get_vehicleInfo(vehicle_id)
    result = []
    for item in data:
        series = pd.Series(item, index=['info_id', 'time', 'status', 'location_id'])

        location = dbFun.get_loc_name(series['location_id'])
        series['station_name'] = location[0][0]
        series['postcode'] = location[0][1]
        series = series.drop("location_id")

        result.append(series)
    return result


# return a dictionary, keys are vehicle id
# values are lists of series containing all infos of corresponding vehicles
# results[1][0], [1] represents for vehicle1, [0]represents for first info of vehicle1
# print(results[1][0])
#
# info_id                     1
# time                        1
# status                 RENTED
# station_name    station_name1
# postcode            postcode1
# dtype: object
def report_all():
    data = dbFun.get_vehicleInfos()
    results = {}
    for item in data.items():
        result = []
        for info in item[1]:
            series = pd.Series(info, index=['info_id', 'time', 'status', 'location_id'])

            location = dbFun.get_loc_name(series['location_id'])
            series['station_name'] = location[0][0]
            series['postcode'] = location[0][1]
            series = series.drop("location_id")

            result.append(series)
        results[item[0]] = result
    return results


def report_period(start_time, end_time):
    data = report_all()
    results = {}
    for item in data.items():
        result = []
        for info in item[1]:
            if (float(info["time"]) >= start_time) & (float(info["time"]) <= end_time):
                result.append(info)
        results[item[0]] = result
    return results
