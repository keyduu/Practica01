import mysql.connector

from database import sql_constants
from classes.mobile_phone import Mobile_phone


def db_connect():
    mydb = mysql.connector.connect(
        host=sql_constants.DB_HOST,
        user=sql_constants.DB_USER,
        database=sql_constants.DB_NAME
    )
    return mydb


def register_mobile_phone(mobile_phone):
    sql = sql_constants.SQL_INSERT
    mydb = db_connect()
    cursor = mydb.cursor()
    val = (mobile_phone.brand, mobile_phone.model, mobile_phone.os, mobile_phone.memory, mobile_phone.price)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()
    return


def get_mobile_phones():
    sql = sql_constants.SQL_SELECT_ALL
    mydb = db_connect()
    cursor = mydb.cursor()
    cursor.execute(sql)
    sql_result_list = cursor.fetchall()
    mydb.disconnect()
    mobile_phones_list = []
    for ele in sql_result_list:
        mobile_phone = Mobile_phone(ele[0], ele[1], ele[2], ele[3], ele[4], float(ele[5]))
        mobile_phones_list.append(mobile_phone)
    return mobile_phones_list


def delete_mobile_phone(mobile_phone_id):
    sql = sql_constants.SQL_DELETE
    mydb = db_connect()
    cursor = mydb.cursor()
    val = (int(mobile_phone_id),)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()
    return


def get_mobile_phone_by_id(mobile_phone_id):
    sql = sql_constants.SQL_SELECT_BY_ID
    mydb: mysql.connector = db_connect()
    cursor = mydb.cursor()
    values = (mobile_phone_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    mydb.disconnect()
    mobile_phone = Mobile_phone(result[0], result[1], result[2], result[3], result[4], float(result[5]))
    return mobile_phone


def update_mobile_phone(mobile_phone):
    sql = sql_constants.SQL_UPDATE
    mydb: mysql.connector = db_connect()
    cursor = mydb.cursor()
    values = (mobile_phone.brand, mobile_phone.model, mobile_phone.os, mobile_phone.memory, mobile_phone.price, mobile_phone.id_mobile_phone)
    cursor.execute(sql, values)
    mydb.commit()
    mydb.disconnect()
    return
