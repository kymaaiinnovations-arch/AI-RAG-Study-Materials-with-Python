# Writing data to a CSV file using csv.writer
import csv

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 20])
    writer.writerow(["Bob", 22])