from src.GeneralQuery import GeneralQuery


class UpdateQuery(GeneralQuery):
    def execute_query(self, cur, query):
        cur.execute(query)
