import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select Id, OrderDate, RequiredDate from "Order" where ShippedDate is null').fetchall()
print(result)