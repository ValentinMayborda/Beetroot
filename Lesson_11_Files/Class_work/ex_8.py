import json

with open('json_data.json', 'r') as f:
    data = json.load(f)

print(data)
print(data.get('dict').get('a'))