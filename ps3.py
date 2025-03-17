number = int(input("Enter a number: "))
print (number * 2)

name = input("Enter your name: ")
print(name.upper())

import random
number = random.randint(10, 20)
guess = None
while guess != number:
    guess = int(input("Guess the number: "))
print("Congratulations!")


age = int(input("Enter your age: "))
if age <= 19:
    print("You qualify for student discounts.")
elif 20 <= age <= 54:
    print("You qualify for no age discounts.")
elif age > 54:
    print("You can receive senior discounts.")

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
number = int(input("Enter a number: "))
print(factorial(number))

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
number = int(input("Enter a number: "))
print(factorial(number))

studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
for name in studentNames:
    print(f"{name} Evans")
newName = input("Enter another name: ")
studentNames.append(newName)
for name in studentNames:
    print(f"{name} Evans")