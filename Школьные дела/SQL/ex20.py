import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
cur.execute('delete from CustomerDemographic where CustomerDesc is null')
connection.commit()