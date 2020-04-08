SQL_INSERCION = "INSERT INTO tabla_moviles(marca, modelo, sistema_operativo, memoria, precio) " \
                "VALUES (%s, %s, %s, %s, %s);"
SQL_CONSULTA = "SELECT * FROM tabla_moviles;"
SQL_BORRAR = "DELETE FROM tabla_moviles WHERE id = %s;"
SQL_CONSULTA_ELEMENTO = "SELECT * FROM tabla_moviles WHERE id = %s;"
