# Open and close a file manually
file = open("sample.txt", "w")
file.write("Hello, World!")
file.write("Hello, World! new text")
file.close()

file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()