import pymysql
from src.ConnectToDB import ConnectToDB


class ConnectToSQLdb(ConnectToDB):
    _instance = None

    @staticmethod
    def get_instance(query_type):
        if ConnectToSQLdb._instance is None:
            return ConnectToSQLdb(query_type)
        else:
            return ConnectToSQLdb._instance

    def __init__(self, query_type):
        if ConnectToSQLdb._instance is None:
            super().__init__(query_type)
            self.connection = pymysql.connect(host='localhost',
                                              user='root',
                                              db='ProjektZaliczeniowy')
        ConnectToSQLdb._instance = self

    def get_cursor(self):
        return self.connection.cursor()

    def close_connection(self):
        print("close")
        self.connection.close()
