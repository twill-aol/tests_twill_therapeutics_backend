import json


string_as_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_format)

key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")