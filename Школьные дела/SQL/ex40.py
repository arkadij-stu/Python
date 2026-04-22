import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select ProductName, CompanyName from Product inner join Supplier on Supplier.Id = Product.SupplierId').fetchall()
print(result)