# import pymysql
# from openpyxl import load_workbook
#
#
# connection = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='just4Taqtile',
#     database='test',
#     cursorclass=pymysql.cursors.DictCursor
# )
# cursor = connection.cursor()
#
# sql = "SELECT * FROM Skany"
# cursor.execute(sql)
#
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# connection.close()


import pyodbc
from openpyxl.reader.excel import load_workbook

####sudo docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=just4Taqtile" -p 1433:1433 --name sql1 --hostname sql1 -d mcr.microsoft.com/mssql/server:2019-latest



# Set up connection parameters
server = '192.168.1.110'
database = 'test'
username = 'sa'
password = 'just4Taqtile'
driver = '{ODBC Driver 17 for SQL Server}' # change this based on your driver

# # Set up connection string
conn_str = f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver};TrustServerCertificate=yes'

# Connect to database
connection = pyodbc.connect(conn_str)

# # Query the database
cursor = connection.cursor()
cursor.execute('SELECT * FROM Skany')
# cursor.execute('SELECT indeks, data, stanowisko, uzytkownik FROM Skany WHERE indeks IN (%s)')

# Fetch results
for row in cursor:
    print(row)

# Close the connection
cursor.close()
connection.close()
