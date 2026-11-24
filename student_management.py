students = []
def add_student():

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    marks = []
    n = int(input("Enter the number of marks u want to add: "))
    for i in range(1,n+1):
        mark = float(input("Enter marks: "))
        marks.append(mark)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    with open("students.txt", "a") as file:
        file.write(name + "," + roll + "," +
                   ",".join(map(str, marks)) + "\n")

    print("Student added successfully!")
def view_students():

    if len(students) == 0:
        print("No students found.")

    else:
        for student in students:

            print("\nName:", student["name"])
            print("Roll Number:", student["roll"])
            print("Marks:", student["marks"])
def search_student():

    roll = input("Enter roll number to search: ")

    for student in students:

        if student["roll"] == roll:
            print("Student Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")
def calculate_average():

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            marks = student["marks"]

            average = sum(marks) / len(marks)

            print("Average Marks:", average)
            return

    print("Student not found.")
try:
    with open("students.txt", "r") as file:

        for line in file:
            data = line.strip().split(",")

            student = {
                "name": data[0],
                "roll": data[1],
                "marks": [
                    float(data[2]),
                    float(data[3]),
                    float(data[4])
                ]
            }

            students.append(student)

except FileNotFoundError:
    pass
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Average Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice!")
