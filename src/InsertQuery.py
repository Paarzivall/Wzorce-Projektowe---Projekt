from src.GeneralQuery import GeneralQuery


class InsertQuery(GeneralQuery):
    def execute_query(self, cur, query):
        cur.execute(query)
