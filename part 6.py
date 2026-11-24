def largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

result = largest(x, y, z)

print("Largest number:", result)

def check_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):

        if n % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if check_prime(number):
    print("Prime Number")

else:
    print("Not a Prime Number")

def calculate_average(marks):

    total = sum(marks)

    average = total / len(marks)

    return average


marks = [80, 90, 75, 85, 70]

result = calculate_average(marks)

print("Average Marks:", result)

def calculate_average(marks):

    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):

    if b == 0:
        return "Division by zero is not possible"

    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", addition(a, b))

elif choice == 2:
    print("Result:", subtraction(a, b))

elif choice == 3:
    print("Result:", multiplication(a, b))

elif choice == 4:
    print("Result:", division(a, b))

else:
    print("Invalid choice")

