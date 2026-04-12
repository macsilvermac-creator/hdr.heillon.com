
with open('C:/hdr.heillon.com/index.html', encoding='utf-8') as f:
    c = f.read()

# Encontrar a secção adopt e ver o que tem
import re
adopt_idx = c.find('id="adopt"')
if adopt_idx == -1:
    adopt_idx = c.find('id=\\"adopt\\"')
print('adopt section at:', adopt_idx)
if adopt_idx >= 0:
    print('snippet:', c[adopt_idx:adopt_idx+600])
