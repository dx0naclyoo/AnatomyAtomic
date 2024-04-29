from slugify import slugify
from anatomic.Backend.Topic import model

random_dict = '{"id": 1, "name": "string", "content": "string", "section_id": 1, "keywords": [], "slug": "string"}'
print(random_dict)
print(model.Topic.parse_raw(random_dict))
# id: int
# name: str
# content: str
# keywords: List[str] = []
# section_id: int
# slug: str

# txt = 'Компьютер по низким ценам'
# r = slugify(txt)
# print(r, type(r))
