# Writing to a file using write() and writelines()
with open("sample.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Verify by reading
with open("sample.txt", "r") as f:
    print(f.read())