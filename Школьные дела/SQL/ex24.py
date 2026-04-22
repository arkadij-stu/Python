import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select ProductName, SupplierId from Product where SupplierId = (select SupplierId from Product where ProductName == "Chang")').fetchall()
print(result)