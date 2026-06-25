# Reading CSV as dictionaries using DictReader
import csv

with open("/data/students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])