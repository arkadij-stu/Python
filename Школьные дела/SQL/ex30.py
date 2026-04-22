import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select CompanyName, Country from Supplier where country in (select Country from Customer)').fetchall()
print(result)