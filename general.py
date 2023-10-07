import dbFun
import sqlite3
import pandas as pd


# "sign_up" for customer
def sign_up(password, fname, lname, email, phnum, bank_acc_nbr):
    dbFun.create_customer(password, fname, lname, email, phnum, bank_acc_nbr)


# "sign up" for manager and operator, user_type is specified in enum_values.py
def sign_up_inner(user_type, password, fname, lname, email, phnum):
    with sqlite3.connect('ShareBikeDB.db') as db:
        cursor = db.cursor()
        sql = ("INSERT INTO {}s(password, fname, lname, email, phnum)"
               "VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(
            user_type, password, fname, lname, email, phnum))
        cursor.execute(sql)
        db.commit()
    db.close()


# sign in with "email" and "password"
def sign_in(user_type, email, password):
    with sqlite3.connect('ShareBikeDB.db') as db:
        cursor = db.cursor()
        sql = "SELECT password FROM \"{}\" WHERE email = \"{}\"".format(user_type, email)
        cursor.execute(sql)
        result = cursor.fetchall()[0][0]
    db.close()
    return password == result
