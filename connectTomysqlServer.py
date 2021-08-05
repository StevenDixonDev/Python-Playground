import mysql.connector

## pip install mysql-connector-python

config = {
  'user': 'root',
  'password': '1234',
  'host': '127.0.0.1',
  'database': 'employeesdb',
  'raise_on_warnings': True
}


cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

cursor.execute("select * from department")

row = cursor.fetchone()
##rows = cursor.fetchall()

while row is not None:
        print(row)
        row = cursor.fetchone()

# for row in rows:
#     print(row)

cursor.close()
cnx.close()