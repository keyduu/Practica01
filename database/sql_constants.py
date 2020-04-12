# datos de conexión.
DB_HOST = "localhost"
DB_USER = "user_app_mobile_phones"
DB_NAME = "db_mobile_phones"

# Sentencias
SQL_INSERT = "INSERT INTO table_mobile_phones(brand, model, os, memory, price) " \
             "VALUES (%s, %s, %s, %s, %s);"
SQL_SELECT_ALL = "SELECT id, brand, model, os, memory, price " \
                 "FROM table_mobile_phones;"
SQL_DELETE = "DELETE FROM table_mobile_phones " \
             "WHERE id = %s;"
SQL_SELECT_BY_ID = "SELECT id, brand, model, os, memory, price " \
                   "FROM table_mobile_phones " \
                   "WHERE id = %s;"
SQL_UPDATE = "UPDATE table_mobile_phones " \
             "SET brand = %s, model = %s, os = %s, memory = %s , price = %s " \
             "WHERE id = %s;"
