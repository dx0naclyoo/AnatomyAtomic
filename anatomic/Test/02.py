from anatomic import sql_tables
from anatomic.Backend.User import model


asd = model.UserRegister(username="Sanya", email="sanya@gmail.com", password="12345")

new_user = sql_tables.User(**asd.dict())
print(new_user)
