import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select CompanyName, Country from Supplier where Country in ("UK", "Germany", "France", "Italy", "Spain")').fetchall()
print(result)