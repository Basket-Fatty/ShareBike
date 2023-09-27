# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:34:26 2023

@author: 17393
"""

# simulated data
# cust_id = 0
# mana_id = 0
# oper_id = 0
# vehicle_id = 0
# info_id = 0
# location_id = 0
# trip_id = 0

import dbFun


class User:
    def __init__(self, password, fname, lname, email, phnum):
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phnum = phnum


class Customer(User):
    def __init__(self, password, fname, lname, email, phnum,
                 cust_id, bank_acc_nbr="", balance=0.0):
        User.__init__(self, password, fname, lname, email, phnum)
        self.cust_id = cust_id
        self.bank_acc_nbr = bank_acc_nbr
        self.balance = balance

    def rent(self, vehicle_id, time, status, location_id, cust_id):
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

        # create new trip, add it to the table
        dbFun.start_trip(cust_id, vehicle_id, time, location_id)

    def returnBike(self, vehicle_id, time, status, location_id, cust_id):
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

        # calculate the charge
        charge = 0

        # create new trip, add it to the table
        dbFun.end_trip(cust_id, time, location_id, charge)

    def report(self, vehicle_id, time, status, location_id):
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

    # def pay():

    def history(self):
        trips = dbFun.get_trips(self.cust_id)
        # UI display


class Manager(User):
    def __init__(self, password, fname, lname, email, phnum, mana_id):
        User.__init__(self, password, fname, lname, email, phnum)
        self.mana_id = mana_id

    def generate(self):
        infos = dbFun.get_vehicleInfos()
        # UI display


class Operator(User):
    def __init__(self, password, fname, lname, email, phnum, oper_id):
        User.__init__(self, password, fname, lname, email, phnum)
        self.oper_id = oper_id

    # def track():

    def charge(self, vehicle_id, time, status, location_id):
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

    def repair(self, vehicle_id, time, status, location_id):
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)

    def move(self, vehicle_id, time, status, location_id):
        # create new vehicleInfo, add it to the table
        dbFun.insert_vehicleInfo(vehicle_id, time, status, location_id)


class Trip:
    def __init__(self, trip_id, cust_id, vehicle_id, start_vehicleInfo, end_vehicleInfo, charge):
        self.trip_id = trip_id
        self.cust_id = cust_id
        self.vehicle_id = vehicle_id
        self.start_vehicleInfo = start_vehicleInfo
        self.end_vehicleInfo = end_vehicleInfo
        self.charge = charge


class Vehicle:
    def __init__(self, vehicle_id, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type


class VehicleInfo:
    def __init__(self, info_id, vehicle_id, time, status, location):
        self.info_id = info_id
        self.vehicle_id = vehicle_id
        self.time = time
        self.status = status
        self.location = location


class Location:
    def __init__(self, location_id, station_name, postcode):
        self.location_id = location_id
        self.station_name = station_name
        self.station_name = station_name
