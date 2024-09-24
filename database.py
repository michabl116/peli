import mariadb
import sys

# Connect to MariaDB Platform
try:
    yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1Peru20243#',
         autocommit=True
         )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = yhteys.cursor()
cur.execute('SELECT name FROM airport where continent = "EU"  ')
for row in cur:
    print(row)