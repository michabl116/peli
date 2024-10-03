
import mysql.connector
import random

def airport_name_city(country):
    try:
        # Conexión a la base de datos
        yh = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='1Peru20243#',
            autocommit=True
        )
        cursor = yh.cursor()

        # Consulta SQL utilizando parámetros para evitar inyección SQL
        sql = """
        SELECT airport.name, airport.municipality 
        FROM airport 
        INNER JOIN country ON country.iso_country = airport.iso_country 
        WHERE country.name = %s
        """
        cursor.execute(sql, (country,))
        airports = cursor.fetchall()

        # Si hay aeropuertos en el resultado
        if airports:
            random_airport = random.choice(airports)  # Selecciona un aeropuerto al azar
            airport_name, municipality = random_airport
            return airport_name, municipality
        else:
            return None  # No se encontraron aeropuertos

    except mysql.connector.Error as err:
        print(f"Error: {err.msg}")

    finally:
        # Cierre de la conexión y el cursor
        if cursor:
            cursor.close()
        if yh:
            yh.close()