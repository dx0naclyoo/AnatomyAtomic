class Postgresql:
    __method = "12"

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @classmethod
    def get_session(cls):
        return 1


asd = Postgresql()
asd.method = "13"
print(asd.method)
