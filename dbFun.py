# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:47:06 2023

@author: 17393
"""

# CREATE TABLE trips (
#     trip_id           INTEGER PRIMARY KEY AUTOINCREMENT
#                               UNIQUE
#                               NOT NULL,
#     cust_id           INTEGER REFERENCES customers (cust_id),
#     vehicle_id        INTEGER REFERENCES vehicles (vehicle_id),
#     start_vehicleInfo INTEGER REFERENCES vehicleInfo (info_id),
#     end_vehicleInfo   INTEGER REFERENCES vehicleInfo (info_id),
#     charge            REAL
# );

# CREATE TABLE vehicleInfo (
#     info_id    INTEGER PRIMARY KEY AUTOINCREMENT
#                        UNIQUE
#                        NOT NULL,
#     vehicle_id INTEGER REFERENCES vehicles (vehicle_id),
#     time       INTEGER,
#     status     TEXT,
#     location   TEXT
# );

import sqlite3

def createDB():
    with sqlite3.connect("ShareBikeDB.db") as db:
        cursor = db.cursor()
        
        cursor.execute("""CREATE TABLE customers (
            cust_id      INTEGER PRIMARY KEY AUTOINCREMENT
                                  NOT NULL
                                  UNIQUE,
            bank_acc_nbr TEXT,
            balance      REAL,
            password     TEXT,
            fname        TEXT,
            lname        TEXT,
            email        TEXT,
            phnum        TEXT
        );""")
        
        cursor.execute("""CREATE TABLE managers (
            mana_id  INTEGER PRIMARY KEY AUTOINCREMENT
                              NOT NULL
                              UNIQUE,
            password TEXT,
            fname    TEXT,
            lname    TEXT,
            email    TEXT,
            phnum    TEXT
        );""")
        
        cursor.execute("""CREATE TABLE operators (
            oper_id  INTEGER PRIMARY KEY AUTOINCREMENT
                              NOT NULL
                              UNIQUE,
            password TEXT,
            fname    TEXT,
            lname    TEXT,
            email    TEXT,
            phnum    TEXT
        );""")
        
        cursor.execute("""CREATE TABLE locations (
            location_id  INTEGER PRIMARY KEY AUTOINCREMENT
                                  UNIQUE
                                  NOT NULL,
            station_name TEXT,
            postcode     TEXT
        );""")
        
        cursor.execute("""CREATE TABLE vehicles (
            vehicle_id   INTEGER PRIMARY KEY AUTOINCREMENT
                                  NOT NULL
                                  UNIQUE,
            vehicle_type TEXT
        );""")
        
    db.close()
