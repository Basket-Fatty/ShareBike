# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:34:26 2023

@author: 17393
"""

# simulated data
# 不同进程之间通信
cust_id = 0
mana_id = 0
oper_id = 0
vehicle_id = 0
info_id = 0
location_id = 0
trip_id = 0

from enum import Enum

class Status(Enum):
    RENTED = 0
    VACANT = 1
    BROKEN = 2
    LOWBATTERY = 3
    
class Type(Enum):
    BIKE = 0
    EBIKE = 1

class User:
    def __init__(self, password, fname, lname, email, phnum):
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phnum = phnum
        
class Customer(User):
    def __init__(self, password, fname, lname, email, phnum,
                 cust_id, bank_acc_nbr="", balance=0.0, trip_list=[]):
        User.__init__(self, password, fname, lname, email, phnum)
        self.cust_id = cust_id
        self.bank_acc_nbr = bank_acc_nbr
        self.balance = balance
        self.trip_list = trip_list
        
    def rent(vehicle_id, time, location):
        global info_id
        info_id += 1
        newInfo = VehicleInfo(info_id, vehicle_id, time, Status.RENTED, location)
        
        # 数据库行 <-----> python
        
        vehicle = db.get(vehicle_id)
        vehicle.Info_list.add(newInfo)
        
    # def returnBike():
        
    # def report():
        
    # def pay():
        
    # def history():
    
class Manager(User):
    def __init__(self, password, fname, lname, email, phnum, mana_id):
        User.__init__(self, password, fname, lname, email, phnum)
        self.mana_id = mana_id
        
    # def generate():
        
class Operator(User):
    def __init__(self, password, fname, lname, email, phnum, oper_id):
        User.__init__(self, password, fname, lname, email, phnum)
        self.oper_id = oper_id
        
    # def track():
        
    # def charge():
        
    # def repair():
        
    # def move():
        
class Trip:
    def __init__(self, trip_id, cust_id, vehicle_id, start_vehicleInfo, end_vehicleInfo, charge):
        self.trip_id = trip_id
        self.cust_id = cust_id
        self.vehicle_id = vehicle_id
        self.start_vehicleInfo = start_vehicleInfo
        self.end_vehicleInfo = end_vehicleInfo
        self.charge = charge
        
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, Info_list=[]):
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        