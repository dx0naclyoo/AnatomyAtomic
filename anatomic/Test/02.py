from slugify import slugify
from anatomic.Backend.Topic import model
from anatomic import sql_tables

from anatomic.Backend.Section import model

asd = model.Section.parse_raw('{"id": 1, "name": string, "description": string, "keywords": [], "slug": string}')
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
