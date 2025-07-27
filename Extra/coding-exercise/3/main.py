files = ["a.txt", "b.txt", "c.txt"]

for file in files:
    fileopen = open(file, "r")
    read = fileopen.read()
    print(read)
