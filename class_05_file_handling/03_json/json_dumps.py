# Convert Python object to JSON string using dumps()
import json

data = {"name": "Alice", "age": 20}
json_string = json.dumps(data, indent=4)
print(json_string)