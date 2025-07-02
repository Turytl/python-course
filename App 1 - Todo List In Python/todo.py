def get_todos():
    with open("todo.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todos = get_todos()

        user_action = user_action[4:]
        todos.append(user_action + "\n")

        with open("todo.txt", "w") as file:
            todos = file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip()}")

    elif user_action.startswith("edit"):
        try:
            edit_number = int(user_action[5:])
            edit_number = edit_number - 1
            new_todo = input("Enter a new todo: ") + "\n"

            todos = get_todos()

            todos[edit_number] = new_todo

            with open("todo.txt", "w") as file:
                todos = file.writelines(todos)
        except ValueError:
            print("Invalid syntax dumbass")

    elif user_action.startswith("complete"):
        try:
            complete_number = int(user_action[9:])
            complete_number = complete_number - 1

            todos = get_todos()

            deleted = todos[complete_number]
            todos.pop(complete_number)

            with open("todo.txt", "w") as file:
                todos = file.writelines(todos)

            print(f"Todo {deleted.strip()} is completed")
        except (ValueError, IndexError):
            print("Invalid syntax dumbass")

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid syntax dumbass")
print("Bye!")
