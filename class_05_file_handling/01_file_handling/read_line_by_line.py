# Reading a file line by line
with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())