# Working with nested JSON data
import json

data = {"student": {"name": "Alice", "courses": ["Math", "Science"]}}
with open("nested.json", "w") as f:
    json.dump(data, f, indent=4)

with open("nested.json", "r") as f:
    loaded = json.load(f)
    print(loaded["student"]["name"])