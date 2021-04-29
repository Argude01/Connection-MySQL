import mysql.connector

class RedSocial:

    def open_connection():
        connection = mysql.connector.connect( host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="db_red_social")
        return connection

    def insert_db(self, data):
        my_connection = open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_usuarios(CORREO, PWD, EDAD) VALUES (%s,%s,%s)"
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()

   