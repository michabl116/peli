import mysql.connector
import random
def continet(continent):
    try:
        yh = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='1Peru20243#',
            autocommit=True
             )
        cursor = yh.cursor()
        sql=f"SELECT airport.ident, airport.name FROM airport where continent='{continent}' "

        cursor.execute(sql)
        airports = cursor.fetchall()
        if airports:  # Check if there are results
            random_airport = random.choice(airports)  # Choose a random airport
            print(random_airport[1])  # Print the 'ident' of the random airport
        else:
            print("No airports found in this continent.")

        cursor.close()
        yh.close()



    except mysql.connector.Error as err:
        print(err.msg)

#continetkusy= input('"UE,NA,SA "\n Valitse  continent: ')
#continet(continetkusy)

def country(country):
    try:
        yh = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='1Peru20243#',
            autocommit=True
             )
        cursor = yh.cursor()
        sql=f"SELECT country.ident, country.name FROM country where continent='{country}' "
        cursor.execute(sql)
        for row in cursor:
            print(row)
        cursor.close()
        yh.close()

    except mysql.connector.Error as err:
        print(err.msg)
    return


