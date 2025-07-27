member = input("Enter a new member: ")

file = open("members.txt", "r")
read = file.read()
file.close()

file = open("members.txt", "w")
file.writelines(read)
file.writelines(member)
file.close()
