import random

try:
    lower_bound = int(input("Enter lower bound: "))
    upper_bound = int(input("Enter upper bound: "))
except (ValueError, TypeError):
    print("Please enter integers only.")
    exit()

random_number = random.randint(lower_bound, upper_bound)
print(f"Random number between {lower_bound} and {upper_bound} is {random_number}.")
