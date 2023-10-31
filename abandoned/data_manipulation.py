import sqlite3

import dbFun


def get_all_loc():
    with sqlite3.connect("../ShareBikeDB.db") as db:
        cursor = db.cursor()
        sql = "SELECT * FROM locations"
        cursor.execute(sql)
        result = cursor.fetchall()
    db.close()
    return result


def track_vehicle():
    # vehicle_dtl = dbFun.track_vehicle_database()
    # for i in vehicle_dtl:
    #     print (i[1])

    test = dbFun.get_vehicleInfos()
    vehicles_status = {}
    all_loc_dict = fetch_all_location_info_in_dict()
    for i in range(1,len(test)+1):
        time = 0
        for j in test[i]:
            if j[1] > time:
                time = j[1]
                formatted_info = [j[0],j[1],j[2],all_loc_dict[j[3]]]
                vehicles_status.update({i: formatted_info})
    return vehicles_status


def update_vehicle_charge(vehicle_id, time, status, location_id):
    dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)


def fetch_all_location_info_in_dict():
    all_loc = get_all_loc()
    all_loc_dict = {}
    for row in all_loc:
        all_loc_dict.update({row[0]: row[1]})
    return all_loc_dict
