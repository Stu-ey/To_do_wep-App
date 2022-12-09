FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    :param filepath: text fue with to-dos
    :return:

    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    param todos_arg: List of items to write out
    param filepath: where to save them
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())

