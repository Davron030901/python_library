"""pprint - CHIROYLI PRINT"""

from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

print(bemor)
# {'ism': 'Alijon Valiyev', 'yosh': 30, 'oila': True, 'farzandlar': ['Ahmad', 'Bonu'], 'allergiya': None, 'dorilar': [{'nomi': 'Analgin', 'miqdori': 0.5}, {'nomi': 'Panadol', 'miqdori': 1.2}]}

pprint(bemor)