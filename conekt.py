import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="just4Taqtile",
  database="test"
)

print(mydb)
