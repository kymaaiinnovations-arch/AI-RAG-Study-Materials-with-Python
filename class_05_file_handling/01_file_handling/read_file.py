# Reading a file using different methods
with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# read() - reads entire file
with open("sample.txt", "r") as f:
    print(f.read())