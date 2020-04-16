import mysql.connector

import database.sql
from classes.mobile_phone import Mobile_phone


# Conecta a la base de datos y devuelve la conexión.
def db_connect():
    mydb = mysql.connector.connect(
            host=database.sql.DB_HOST,
            port=database.sql.DB_PORT,
            user=database.sql.DB_USER,
            password=database.sql.DB_PASSWORD,
            database=database.sql.DB_NAME
            )
    return mydb


# Añade un teléfono móvil a la base de datos y devuelve el id del registro insertado.
def register_mobile_phone(mobile_phone):
    sql = database.sql.SQL_INSERT
    mydb = db_connect()
    cursor = mydb.cursor()
    val = (mobile_phone.brand, mobile_phone.model, mobile_phone.os, mobile_phone.memory, mobile_phone.price, mobile_phone.technology, mobile_phone.deal, mobile_phone.photo_path)
    cursor.execute(sql, val)

    mydb.commit()
    id = cursor.lastrowid
    mydb.disconnect()
    return id


# Obtiene toda la lista de teléfonos móviles que hay en la base de datos
def get_mobile_phones():
    sql = database.sql.SQL_SELECT_ALL
    mydb = db_connect()
    cursor = mydb.cursor()
    cursor.execute(sql)
    sql_result_list = cursor.fetchall()
    mydb.disconnect()
    mobile_phones_list = []
    for ele in sql_result_list:
        mobile_phone = Mobile_phone(ele[0], ele[1], ele[2], ele[3], ele[4], float(ele[5]), ele[6], ele[7], ele[8])
        mobile_phones_list.append(mobile_phone)
    return mobile_phones_list


# Elimina de la base de datos el teléfono móvil con el identificador facilitado.
def delete_mobile_phone(mobile_phone_id):
    sql = database.sql.SQL_DELETE
    mydb = db_connect()
    cursor = mydb.cursor()
    val = (mobile_phone_id,)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()
    return


# Obtiene de la base de datos el teléfono móvil con el identificador facilitado.
def get_mobile_phone_by_id(mobile_phone_id):
    sql = database.sql.SQL_SELECT_BY_ID
    mydb: mysql.connector = db_connect()
    cursor = mydb.cursor()
    values = (mobile_phone_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    mydb.disconnect()
    mobile_phone = Mobile_phone(result[0], result[1], result[2], result[3], result[4], float(result[5]), result[6],
                                result[7], result[8])
    return mobile_phone


# Modifica en la base de datos el teléfono móvil facilitado.
def update_mobile_phone(mobile_phone):
    sql = database.sql.SQL_UPDATE
    mydb: mysql.connector = db_connect()
    cursor = mydb.cursor()
    values = (mobile_phone.brand, mobile_phone.model, mobile_phone.os, mobile_phone.memory, mobile_phone.price,
              mobile_phone.technology, mobile_phone.deal, mobile_phone.photo_path, mobile_phone.id_mobile_phone)
    cursor.execute(sql, values)
    mydb.commit()
    mydb.disconnect()
    return
