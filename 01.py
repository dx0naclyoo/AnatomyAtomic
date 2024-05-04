from pydantic import BaseModel


class Sect(BaseModel):
    id: int
    name: str


qwe = "{" + '"id": 1, "name": "qweqwe \n qweqwe"'.replace("\n", "=Q1") + "}"
dict_obx = eval(qwe)
new_model = Sect.parse_obj(dict_obx)

print("До", new_model)

for x in new_model:
    key, value = x
    print(value, type(value), end="\n")
    if isinstance(value, str):
        setattr(new_model, key, value.replace("=Q1", "\n"))


print("После", new_model)

