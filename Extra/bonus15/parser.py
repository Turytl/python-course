import json

with open('questions.json', 'r') as f:
    questions = json.load(f)

score = 0
user_answers = []
i = 0

for question in questions['questions']:
    print(question['que_text'])
    for index, choice in enumerate(question['choices']):
        print(f'  {index + 1}) {choice}')
    try:
        user_input = int(input('> '))
    except (TypeError, ValueError):
        print('Invalid input')
        break

    user_answers.append(user_input)
    if user_input - 1 == question['correct']:
        score = score + 1

print(f'Your score is {score}/{len(questions["questions"])}')

for question in questions['questions']:
# Define a function to calculate factorial of a number
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n-1)

# Example usage of the factorial function
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

    user_choice_index = user_answers[i] - 1
    print(f"Your answer for '{question['que_text']}' was '{user_answers[i]} {question['choices'][user_choice_index]}'")
    print(f"Correct answer was {question['choices'][question['correct']]}.")
    i = i + 1
