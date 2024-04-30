class A:
    def __init__(self, *args, level: int = None, items: int = None, **kwargs):
        self.level = level
        self.items = items
        self.args = args
        self.kwargs = kwargs


class B:
    def __init__(self, *args, level: int = None, items: int = None, **kwargs):
        self.level = level
        self.items = items
        self.args = args
        self.kwargs = kwargs


map_class = {"1": A, "2": B}

input_class__ = input("Введите класс (1, 2, 3): ")
input_data = input("Введите информацию (level=10, item=12): ")

if input_class__ in map_class.keys():
    class__ = map_class[input_class__]
    data_list = input_data.split(" ")
    data_in_class__ = {}
    for item in data_list:
        item_list = item.split("=")
        key = item_list[0]
        value = item_list[1]
        data_in_class__[key] = int(value) if value.isnumeric() else value

    asd = A(**data_in_class__)
    print(asd.__dict__)
