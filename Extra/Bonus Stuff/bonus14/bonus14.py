from func import convert, parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed[0], parsed[1])

print(f"{parsed[0]} feet and {parsed[1]} inches is {result} meters.")

if result < 1:
    print("tiny ass")
else:
    print("not tiny ass")
