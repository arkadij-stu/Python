import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select ProductName from Product where Id in (select ProductId from OrderDetail)').fetchall()
print(result)