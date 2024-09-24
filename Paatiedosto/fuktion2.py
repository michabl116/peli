import mysql.connector
from mysql.connector import Error
def date(first_name, last_name,age ):
    try:
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


            query = "insert into player_information(first_name,last_name, age)VALUES(%s, %s, %s)"
            valores = (first_name, last_name, age)

            # Ejecutar la query
            cursor.execute(query, valores)

            # Confirmar la transacción
            yh.commit()

            print("Datos insertados correctamente.")

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")

    finally:
        if yh.is_connected():
            cursor.close()
            yh.close()



