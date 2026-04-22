import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select ProductName, UnitPrice from Product where UnitPrice > (select UnitPrice from Product where ProductName = "Ikura")').fetchall()
print(result)