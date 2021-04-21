import pyodbc

con = pyodbc.connect(Trusted_Connection='Yes',DRIVER='{SQL Server}',SERVER='localhost',DATABASE='dev')
cursor = con.cursor()
cursor.execute("select * from customers")
rows = cursor.fetchall()

