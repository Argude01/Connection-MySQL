import mysql.connector

connection = mysql.connector.connect(host="localhost", 
                                    user="root", 
                                    passwd="", 
                                    database="db_red_social")

cursor = connection.cursor()
query = "INSERT INTO tbl_usuarios(CORREO, PWD, EDAD) VALUES (%s,%s,%s)"
data = ("reader@gmail.com", "supervisor", 20)
cursor.execute(query, data)

connection.commit()
connection.close()    