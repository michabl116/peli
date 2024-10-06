"""import mysql.connector
from mysql.connector import Error

def date_goal(first_name, level, cont, city2, ident):
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

            # Limpiar o actualizar datos antiguos antes de insertar nuevos
            # Puedes modificar esta consulta según tus necesidades (e.g., borrar, actualizar)
            clean_query = "UPDATE player_goal SET continet = NULL, airport_name = NULL WHERE ident = %s"
            cursor.execute(clean_query, (ident,))
            yh.commit()

            # Insertar nuevos datos
            insert_query = """
            INSERT INTO player_goal (first_name, player_level, continet, airport_name, ident) 
            VALUES (%s, %s, %s, %s, %s)
            """
            new_values = (first_name, level, cont, city2, ident)

            cursor.execute(insert_query, new_values)
            yh.commit()

            print("DATA INSERTED AND CLEANED CORRECTLY.")

    except Error as e:
        print(f"Error connecting to database: {e}")
        if yh.is_connected():
            yh.rollback()

    finally:
        if yh.is_connected():
            cursor.close()
            yh.close()



            
def date_goal(first_name, level, cont, city2, ident):
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

            # Limpiar solo la columna continet
            clean_query = "UPDATE player_goal SET continet = NULL WHERE ident = %s"
            cursor.execute(clean_query, (ident,))
            yh.commit()

            # Insertar nuevos datos
            insert_query = """
            INSERT INTO player_goal (first_name, player_level, continet, airport_name, ident) 
            VALUES (%s, %s, %s, %s, %s)
            """
            new_values = (first_name, level, cont, city2, ident)

            cursor.execute(insert_query, new_values)
            yh.commit()

            print("DATA INSERTED AND CLEANED CORRECTLY.")

    except Error as e:
        print(f"Error connecting to database: {e}")
        if yh.is_connected():
            yh.rollback()

    finally:
        if yh.is_connected():
            cursor.close()
            yh.close()
            """
import mysql.connector
from mysql.connector import Error

def incrementar_columna(ident,player_points):
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

            # Incrementar el valor de la columna "score"
            incrementar_query = "UPDATE player_goal SET player_points = player_points + %s WHERE ident = %s"
            cursor.execute(incrementar_query, (player_points, ident))
            yh.commit()

            print("Valor incrementado correctamente.")

    except Error as e:
        print(f"Error connecting to database: {e}")
        if yh.is_connected():
            yh.rollback()

    finally:
        if yh.is_connected():
            cursor.close()
            yh.close()