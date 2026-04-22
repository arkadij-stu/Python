import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select LastName, FirstName, City from Employee where City = (select City from Employee where Id = "5")').fetchall()
print(result)