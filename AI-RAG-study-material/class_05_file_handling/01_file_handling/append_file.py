# Appending data to an existing file
with open("log.txt", "a") as f:
    f.write("New log entry\n")
    f.write("Teacher is Kartik\n")

with open("log.txt", "r") as f:
    print(f.read())