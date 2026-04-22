import sqlite3
connection = sqlite3.connect('northwind_small.sqlite')
cur = connection.cursor()
result = cur.execute('select RegionDescription from Region where Id in (select RegionId from Territory)').fetchall()
print(result)