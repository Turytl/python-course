def read_file(filename):
    # this is a comment
    '''yeah idk what im supposed to write here but sure'''
    with open(filename, "r") as file_local:
        todos_local = file_local.read()
        return todos_local

print(read_file("test.txt"))
print(help(read_file))
