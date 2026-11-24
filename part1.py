print("Hello, World!")

print("Name: Anish Manna")
print("Branch: B.Tech in AI-DS")
print("Year: First Year")
print("Introduction: I am a technology enthusiast who is also fond of music.")

name = "Anish Manna"
roll_number = "26UAD160"
age = 19
cgpa = 8.5

print("Student Name:", name)
print("Roll Number:", roll_number)
print("Age:", age)
print("CGPA:", cgpa)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_result = a + b
difference = a - b
product = a * b

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)

if b != 0:
    quotient = a / b
    print("Quotient:", quotient)
else:
    print("Division by zero is not possible.")

age = 19
cgpa = 8.5
name = "Anish"
is_student = True

print(age)
print(cgpa)
print(name)
print(is_student)

print(type(age))
print(type(cgpa))
print(type(name))
print(type(is_student))

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

x = 15

print(x > 10 and x < 20)
print(x > 20 or x < 20)
print(not(x > 20))