from abc import ABC, abstractmethod


class DatabaseSQL(ABC):
    @classmethod
    @abstractmethod
    def get_session(cls):
        pass

    @abstractmethod
    def get(self, table, item_id):
        pass

    @abstractmethod
    def get_all(self, table):
        pass

    @abstractmethod
    def add(self, table, item):
        pass

    @abstractmethod
    def update(self, table, item_id, item):
        pass

    @abstractmethod
    def delete(self, table, item_id):
        pass


class Postgresql(DatabaseSQL):
    def __init__(self):
        pass

    @classmethod
    def get_session(cls):
        pass

    def get(self, table, item_id):
        pass

    def get_all(self, table):
        pass

    def add(self, table, item):
        pass

    def update(self, table, item_id, item):
        pass

    def delete(self, table, item_id):
        pass
