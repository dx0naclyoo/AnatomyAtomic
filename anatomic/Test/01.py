class Postgresql:
    @classmethod
    def get_session(cls):
        return 1


print(Postgresql.get_session())
