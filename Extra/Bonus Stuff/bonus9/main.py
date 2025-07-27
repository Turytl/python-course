password = input("Enter password: ")
result = []

if len(password) >=8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

digit = False
for i in password:
    if i.isupper():
        digit = True

result.append(digit)

if result.count(True) == 3:
    print("Strong password")
else:
    print("Weak password")
