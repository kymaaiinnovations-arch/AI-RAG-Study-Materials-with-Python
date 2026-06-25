# Using 'with' statement for automatic file handling
with open("sample.txt", "w") as f:
    f.write("Auto-closed file\n")

with open("sample.txt", "r") as f:
    print(f.read())  # File auto-closes after block