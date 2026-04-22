import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select FirstName, LastName, HireDate from Employee where HireDate > (select HireDate from Employee where LastName = "Davolio" and FirstName = "Nancy")').fetchall()
print(result)