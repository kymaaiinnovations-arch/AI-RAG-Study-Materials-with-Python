# Parse JSON string using loads()
import json

json_string = '{"name": "Alice", "age": 20}'
data = json.loads(json_string)
print(data["name"])