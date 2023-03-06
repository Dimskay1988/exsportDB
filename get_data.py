import pymysql
from openpyxl import load_workbook


connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='just4Taqtile',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = connection.cursor()

sql = "SELECT * FROM Skany"
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
