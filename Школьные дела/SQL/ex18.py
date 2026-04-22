import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
cur.execute('update Supplier set ContactName = "Иван Иванов" where CompanyName = "Exotic Liquids"')
connection.commit()