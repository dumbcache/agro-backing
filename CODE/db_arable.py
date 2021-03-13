import json
with open('datasets/arable.json') as f:
    c=json.load(f)
print(c.keys())