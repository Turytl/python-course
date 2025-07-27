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

