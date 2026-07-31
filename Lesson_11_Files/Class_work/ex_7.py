import json

d = {'a': 1}
l = [1, 2.4]
t = (3, 4, 5)
s = 'Hello world'
b = True
st = {1, 2, 'Test'}
print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))
print(json.dumps(b))
obj = {'tuple': t, 'list': l, 'dict': d, 'string': s, 'bool': b}
# print(json.dumps(st))

with open('json_data.json', 'w') as f:
    json.dump(obj, f)