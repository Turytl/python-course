def get_todos(filename="todo.txt"):
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos, filename="todo.txt"):
    with open(filename, "w") as file_local:
        file_local.writelines(todos)


def user_action_function():
    user_action_local = input("Type add, show, complete, edit or exit: ").strip()
    return user_action_local

while True:
    user_action = user_action_function()

    if user_action.startswith("add"):
        todos = get_todos()

        todos.append(user_action[4:] + "\n")
        
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip()}")

    elif user_action.startswith("edit"):
        try:
            edit_number = int(user_action[5:]) - 1
            new_todo = input("Enter a new todo: ") + "\n"

            todos = get_todos()

            todos[edit_number] = new_todo

            write_todos(todos)

        except ValueError:
            print("Invalid Syntax.")

    elif user_action.startswith("complete"):
        try:
            complete_number = int(user_action[9:]) - 1

            todos = get_todos()

            deleted = todos[complete_number]
            todos.pop(complete_number)

            write_todos(todos)

            print(f"Todo {deleted.strip()} is completed")
        except (ValueError, IndexError):
            print("Invalid Syntax.")

    elif user_action.startswith("exit"):
        print("Bye")
        break

    else:
        print("Invalid Syntax.")
