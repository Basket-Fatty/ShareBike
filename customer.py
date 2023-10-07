import pandas as pd
import dbFun
import enum_values


def rent(vehicle_id, time, status, location_id, cust_id):
    # create new vehicleInfo, add it to the table
    status = enum_values.Status.RENTED
    dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

    # create new trip, add it to the table
    dbFun.start_trip(cust_id, vehicle_id, time, location_id)


def returnBike(vehicle_id, time, status, location_id, cust_id):
    # create new vehicleInfo, add it to the table
    status = enum_values.Status.VACANT
    dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

    # calculate the charge
    charge = 0

    # create new trip, add it to the table
    dbFun.end_trip(cust_id, time, location_id, charge)


def report(vehicle_id, time, status, location_id):
    # create new vehicleInfo, add it to the table
    dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)


def pay():
    return


# return a list of series containing all trips of a customer
# print(result[0])

# trip_id                         1.0
# vehicle_id                      1.0
# start_time                     12.0
# end_time                       15.0
# charge                          9.0
# start_station_name    station_name1
# start_postcode            postcode1
# end_station_name      station_name3
# end_postcode              postcode3
# dtype: object
def history(cust_id):
    trips_list = dbFun.get_trips(cust_id)
    result = []
    for trip in trips_list:
        series = pd.Series(trip, index=['trip_id', 'vehicle_id', 'start_time', 'start_location_id', 'end_time',
                                        'end_location_id', 'charge'])

        start_location = dbFun.get_loc_name(series['start_location_id'])
        series['start_station_name'] = start_location[0][0]
        series['start_postcode'] = start_location[0][1]
        end_location = dbFun.get_loc_name(series['end_location_id'])
        series['end_station_name'] = end_location[0][0]
        series['end_postcode'] = end_location[0][1]

        series = series.drop('start_location_id')
        series = series.drop('end_location_id')
        result.append(series)
    return result
