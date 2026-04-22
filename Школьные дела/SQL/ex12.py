import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select Id, CustomerId, Freight from "Order" where Freight > 100 order by Freight DESC').fetchall()
print(result)