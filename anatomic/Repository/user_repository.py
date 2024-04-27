from anatomic.Database.database import Postgresql
from base import BaseRepository
from anatomic import sql_tables


class UserRepository(BaseRepository):
    def __init__(self):
        self.database = Postgresql()
        self.session = Postgresql.get_session()
        self.table = sql_tables.User

    def get_user_by_id(self, user_id):
        self.database.get(self.table, user_id)

    def get_all_users(self):
        pass

    def add_user(self, user):
        pass

    def update_user(self, user):
        pass

    def delete_user(self, user_id):
        pass
