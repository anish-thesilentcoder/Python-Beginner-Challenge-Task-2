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