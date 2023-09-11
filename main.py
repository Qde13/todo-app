#from functions import get_todos, write_todos
import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4: ]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        #new_todos = [item.strip('\n') for  item in todos]     # List of comprehensions

        for index, item in enumerate(todos):                   # Change todos to ne_todos
            item = item.strip('\n')                            # Delete or comment
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("write new value: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_complete = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo {todo_to_complete} was removed from the list'
            print(message)
        except IndexError:
            print("There is no item with number.")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")

print('Bye!')
