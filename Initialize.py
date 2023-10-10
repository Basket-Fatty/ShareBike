# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:17:38 2023

@author: 17393
"""
import dbFun
import enum_values
import customer
import employee
import general
import manager

dbFun.create_db()
dbFun.create_vehicle("E-Bike", 12, 1)
dbFun.create_vehicle("Bike", 12, 2)
dbFun.create_vehicle("Bike", 12, 3)

dbFun.create_location("station_name1", "postcode1")
dbFun.create_location("station_name2", "postcode2")
dbFun.create_location("station_name3", "postcode3")

general.sign_up("password1", "fname1", "lname1", "email1", "phnum1", "bank_acc_nbr1")
general.sign_up("password2", "fname2", "lname2", "email2", "phnum2", "bank_acc_nbr2")
general.sign_up("password3", "fname3", "lname3", "email3", "phnum3", "bank_acc_nbr3")

# customer1 travel from location1 to location3 with vehicle1
customer.rent(1, 12, 1, 1)
customer.returnBike(1, 15, 3, 1)
# report low power
customer.report(1, 15, enum_values.Status.LOWPOWER.value, 3)
# customer1 pay 3 pounds
customer.pay(1, 3)
# check the trip history of customer1
print("customer1 travel history:")
data = customer.history(1)
for item in data:
    print(item)

print()
# operator charge the bike, move it to location2
employee.charge(1, 16, 3)
employee.move(1, 17, 2)
# track the latest information of all vehicles
print("employee track:")
data = employee.track()
for item in data.items():
    print("vehicle" + str(item[0]))
    print(item[1])

print()
# manager check all the infomation of all vehicles
print("manager report:")
data = manager.report_all()
for item in data.items():
    print("vehicle" + str(item[0]))
    for element in item[1]:
        print(element)
    print()
