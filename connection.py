import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",passwd="")

cursor1 = connection.cursor()
cursor1.execute("show databases")
for base in cursor:
    print(base)
connection.close()  



