import mysql.connector
from mysql.connector import Error

def date_talenta(first_name, level, cont, city2, ident):
    try:
        # Conexión a la base de datos
        yh = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='airportgame',
            user='root',
            password='1Peru20243#',
            autocommit=True
        )

        if yh.is_connected():
            cursor = yh.cursor()

            # Consulta de inserción
            query = "INSERT INTO player_goal (first_name, player_level, continet, airport_name, ident) VALUES (%s, %s, %s, %s, %s)"
            valores = (first_name, level, cont, city2, ident)

            # Ejecutar la consulta
            cursor.execute(query, valores)
            yh.commit()

            print("DATA INSERTED CORRECTLY..")

    except Error as e:
        # En caso de error, mostrar mensaje y hacer rollback
        print(f"Error connecting to database: {e}")
        if yh.is_connected():
            yh.rollback()

    finally:
        # Cerrar la conexión
        if yh.is_connected():
            cursor.close()
            yh.close()