import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select FirstName, LastName from Employee where Id in (select EmployeeId from EmployeeTerritory)').fetchall()
print(result)