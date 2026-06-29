# Writing CSV using DictWriter
import csv

with open("output.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age", "city", "school"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 20})
    writer.writerow({"Name": "Rajat", "Age": 24, "city": "Agartala", "school":"NIT Agartala"})