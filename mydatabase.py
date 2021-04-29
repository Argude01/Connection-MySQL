import mysql.connector

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_red_social")
        return connection

    def insert_db(self, email, pwd, age):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_usuarios(CORREO, PWD, EDAD) VALUES (%s,%s,%s)"
        query2 = "INSERT INTO tbl_gallery(CORREO, PWD, EDAD) VALUES (%s,%s,%s)"
        
        data = (email, pwd, age)
        cursor.execute(query, data)

        cursor2 = my_connection.cursor()
        cursor2.execute(query2, data)
        my_connection.commit()
        my_connection.close()


   