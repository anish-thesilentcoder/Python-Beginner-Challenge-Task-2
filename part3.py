number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

elif marks >= 60:
    print("Grade D")

elif marks >= 40:
    print("Grade E")

else:
    print("Fail")

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("Not a Leap Year")

elif year % 4 == 0:
    print("Leap Year")

else:
    print("Not a Leap Year")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")
