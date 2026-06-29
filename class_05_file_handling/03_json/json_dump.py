# Write Python object to JSON file using dump()
import json

data = {"name": "Alice", "age": 20}
data["city"] = "Agartala"

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)