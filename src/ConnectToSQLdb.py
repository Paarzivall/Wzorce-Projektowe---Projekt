import pymysql
from src.ConnectToDB import ConnectToDB


class ConnectToSQLdb(ConnectToDB):
    def __init__(self, query_type):
        super().__init__(query_type)
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          db='ProjektZaliczeniowy',
                                          autocommit=True)
        self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor

    def close_cursor(self):
        return self.cursor.close()

    def close_connection(self):
        print("close")
        self.connection.close()
