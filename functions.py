def get_todos(filename="todos.txt"):
    """ Read a text file todos.txt and return the list of
    to-do items.
    """
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename="todos.txt"):
    """ Write the to-do items list in the text file todos.txt."""
    with open(filename, 'w') as file_local:
        file_local.writelines(todos_arg)

