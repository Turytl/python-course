while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        with open("todo.txt", "r") as file:
            todos = file.readlines()

        user_action = user_action[4:]
        todos.append(user_action + "\n")

        with open("todo.txt", "w") as file:
            todos = file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todo.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip()}")

    elif user_action.startswith("edit"):
        try:
            edit_number = int(user_action[5:])
            edit_number = edit_number - 1
            new_todo = input("Enter a new todo: ") + "\n"

            with open("todo.txt", "r") as file:
                todos = file.readlines()

            todos[edit_number] = new_todo

            with open("todo.txt", "w") as file:
                todos = file.writelines(todos)
        except ValueError:
            print("Invalid syntax dumbass")

    elif user_action.startswith("complete"):
        try:
            complete_number = int(user_action[9:])
            complete_number = complete_number - 1

            with open("todo.txt", "r") as file:
                todos = file.readlines()

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
