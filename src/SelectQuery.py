from src.GeneralQuery import GeneralQuery


class SelectQuery(GeneralQuery):
    def execute_query(self, cur, query):
        cur.execute(query)
        return cur.fetchall()
