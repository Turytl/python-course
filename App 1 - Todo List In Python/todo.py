import functions

while True:
    user_action = functions.user_action_function()

    if user_action.startswith("add"):
        todos = functions.get_todos()

        todos.append(user_action[4:] + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip()}")

    elif user_action.startswith("edit"):
        try:
            edit_number = int(user_action[5:]) - 1
            new_todo = input("Enter a new todo: ") + "\n"

            todos = functions.get_todos()

            todos[edit_number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Invalid Syntax.")

    elif user_action.startswith("complete"):
        try:
            complete_number = int(user_action[9:]) - 1

            todos = functions.get_todos()

            deleted = todos[complete_number]
            todos.pop(complete_number)

            functions.write_todos(todos)

            print(f"Todo {deleted.strip()} is completed")
        except (ValueError, IndexError):
            print("Invalid Syntax.")

    elif user_action.startswith("exit"):
        print("Bye")
        break

    else:
        print("Invalid Syntax.")
