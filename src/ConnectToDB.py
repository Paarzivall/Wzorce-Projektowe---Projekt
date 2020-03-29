from abc import ABC, abstractmethod


class ConnectToDB(ABC):
    def __init__(self, query_type):
        self.database = query_type

    def execute_query(self, cur, sql):
        return self.database.execute_query(cur, sql)