# Load JSON from a file
import json

# Create a JSON file first
with open("data.json", "w") as f:
    f.write('{"name": "Alice", "age": 20}')

with open("data.json", "r") as f:
    data = json.load(f)
    print(data)