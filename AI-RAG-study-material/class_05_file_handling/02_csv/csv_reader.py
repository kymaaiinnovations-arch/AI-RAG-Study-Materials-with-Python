# Reading a CSV file using csv.reader
import csv

with open("../data/students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)