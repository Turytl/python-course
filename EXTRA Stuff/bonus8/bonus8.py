date = input("Enter date in format dd/mm/yyyy : ")
mood = input("Enter mood from 1 to 10 : ")
thought = input("Enter thought : " + "\n")

format = f"../journal/{date}.txt"

with open(format, "w") as file:
    file.write(f"{mood}\n\n")
    file.write(thought)
