subjects = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Computer Science",
    "English"
]

for subject in subjects:
    print(subject)

marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
average = total / 5
highest = max(marks)
lowest = min(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

student = {
    "name": "Anish Manna",
    "roll_number": 101,
    "marks": 85
}

print("Student Name:", student["name"])
print("Roll Number:", student["roll_number"])
print("Marks:", student["marks"])

names = ["Anish", "Rahul", "Aman", "Rohit", "Sourav"]

search_name = input("Enter name to search: ")

if search_name in names:
    print("Name found in the list")
else:
    print("Name not found in the list")

text = input("Enter a string: ")

frequency = {}

for ch in text:

    if ch in frequency:
        frequency[ch] = frequency[ch] + 1

    else:
        frequency[ch] = 1

print("Character frequency:")

for ch, count in frequency.items():
    print(ch, ":", count)