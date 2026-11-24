for i in range(1, 101):
    print(i)

i = 1
while i <= 100:
    print(i)
    i = i + 1

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

n = int(input("Enter the value of N: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum =", sum)

word = input("Enter a word: ")
count = 0
for ch in word.lower():
    if ch in "aeiou":
        count = count + 1
print("Number of vowels:", count)

for num in range(2, 101):

    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
