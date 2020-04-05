import mysql.connector
from base_datos import constantes
from clases.movil import Movil


def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user_app_moviles",
        database="bd_moviles"
    )
    return mydb


def registro_movil(movil):
    sql = constantes.SQL_INSERCION
    mydb = conectar()
    cursor = mydb.cursor()
    val = (movil.marca, movil.modelo, movil.sistema_operativo, movil.memoria, movil.precio)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()


def obtener_moviles():
    sql = constantes.SQL_CONSULTA
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql)
    resultado_lista = cursor.fetchall()
    mydb.disconnect()
    return resultado_lista
