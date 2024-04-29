
from slugify import slugify


txt = 'Компьютер по низким ценам'
r = slugify(txt)
print(r, type(r))
