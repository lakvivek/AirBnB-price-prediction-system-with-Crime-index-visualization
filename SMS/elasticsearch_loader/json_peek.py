import json
from pprint import pprint

file = "../data/processed_NYPD"


with open('../data/{}.json'.format(file)) as f:
    data = json.load(f)

pprint(data[0:4])