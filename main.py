import config.database

while True:
    config.database.print_info()
    choice = input("Enter your choice: ")
    if choice == '1':
        config.database.add_students()
    elif choice == '2':
        config.database.view_students()
    elif choice == '3':
        config.database.edit_student()
    elif choice == '4':
        config.database.delete_student()
    else:
        break