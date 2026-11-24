file = open("myfile.txt", "w")

file.write("Hello! Welcome to Python programming.")

file.close()


file = open("myfile.txt", "r")

content = file.read()

print(content)

file.close()

with open("myfile.txt", "w") as file:
    file.write("Hello! Welcome to Python programming.")

with open("myfile.txt", "r") as file:
    content = file.read()

print(content)

name = input("Enter student name: ")
marks = input("Enter student marks: ")

with open("student.txt", "w") as file:

    file.write("Student Name: " + name + "\n")

    file.write("Student Marks: " + marks)


with open("student.txt", "r") as file:

    data = file.read()

print("\nSaved Student Information:")
print(data)

try:

    number = int(input("Enter a number: "))

    print("You entered:", number)

except ValueError:

    print("Invalid input! Please enter a valid integer.")

filename = "student.txt"

try:

    with open(filename, "r") as file:

        data = file.read()

        if data.strip() == "":
            print("The file is empty.")

        else:
            print("File contents:")
            print(data)

except FileNotFoundError:

    print("File does not exist.")

