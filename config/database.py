import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sample"
)

mycursor = mydb.cursor()

sql_create = "INSERT INTO students (name, age) VALUES (%s, %s)"
sql_select = "SELECT * FROM students"
sql_view = "SELECT FROM students WHERE id = %s"
sql_edit = "UPDATE students SET name = %s, age = %s WHERE id = %s"
sql_delete = "DELETE FROM students where id = %s"


def add_students():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    value =(name,age)
    mycursor.execute(sql_create, value)
    mydb.commit()
    print("Student has been added")


def view_students():
    mycursor.execute(sql_select)
    result = mycursor.fetchall()
    for iteration, item in enumerate(result, start=1):
        print(f"{iteration} . Name: {item[1]}, Age: {item[2]}")


def edit_student():
    id_input = int(input("Enter student id: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    value=(name,age,id_input)
    mycursor.execute(sql_edit, value)
    mydb.commit()
    print("Student has been updated")


def delete_student():
    id_input = int(input("Enter student id: "))
    mycursor.execute(sql_delete, (id_input,))
    mydb.commit()
    print("Student has been deleted")


def print_info():
    print("Student Management System")
    print("1 - Add Student")
    print("2 - View Students")
    print("3 - Edit Student")
    print("4 - Delete Student")
    print("5 - Exit")
