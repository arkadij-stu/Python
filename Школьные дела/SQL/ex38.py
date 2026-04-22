import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select ProductName, CategoryName from Product inner join Category on Product.CategoryId = Category.Id').fetchall()
print(result)