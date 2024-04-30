from slugify import slugify
from anatomic.Backend.Topic import model
from anatomic import sql_tables

from anatomic.Backend.Section import model
raw = '{"id": 10, "name": "мышцы", "description": "Раздел анатомии о мышцых человека", "keywords": ["asd", "zxc", "asd"], "slug": "myshtsy"}'
asd = eval('"id": 6, "name": "Понятное имя", "content": "string", "section_id": 1, "keywords": [], "slug": "poniatnoe-imia"')
print(asd)

# id: int
# name: str
# content: str
# keywords: List[str] = []
# section_id: int
# slug: str

# txt = 'Компьютер по низким ценам'
# r = slugify(txt)
# print(r, type(r))
