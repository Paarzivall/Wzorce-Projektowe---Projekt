from abc import ABC, abstractmethod


class GeneralQuery(ABC):
    @abstractmethod
    def execute_query(self, cur, query):
        pass
