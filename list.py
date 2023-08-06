data = []


def print_definition():
    print("TASK MANAGEMENT SYSTEM")
    print("1 - Add Task")
    print("2 - Edit Task")
    print("3 - View all Tasks")
    print("4 - Delete a task")
    print("5 - Exit")


def show():
    print("Tasks are: ")
    for iteration, item in enumerate(data):
        print(f"{iteration + 1} . {item}")
    print("")


def store():
    data_input = input("Enter task: ")
    data.append(data_input)
    print("Task has been added")
    print("")


def edit():
    id_input = int(input("Specify the number of task: "))
    index = id_input - 1
    data.pop(index)
    data_input = input("Enter new task name: ")
    data.insert(index, data_input)
    print("Task has been updated")
    print("")


def delete():
    id_input = int(input("Specify the number of task: "))
    index = id_input - 1
    data.pop(index)
    print("Task has been deleted")
    print("")


while True:
    print_definition()
    choice = input("Enter your choice:")
    if choice == '1':
        store()
    elif choice == '2':
        edit()
    elif choice == '3':
        show()
    elif choice == '4':
        delete()
    elif choice == '5':
        break
