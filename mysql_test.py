import mysql.connector



class DatabaseConnection:
    def __init__(self, host = "localhost", user="root", password="root", database = "school"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = mysql.connector.connect(host=self.host, user=self.user,
                                             password=self.password, database=self.database)
        return connection

connection = DatabaseConnection().connect()
cursor = connection.cursor()
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
print(result)

