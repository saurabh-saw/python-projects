# # Control flow and logical operators
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you ride")

# """
# Other camparision operators:
# >, <, >=, <=, ==, !=
# """

# # Modulo
# n = int(input("Enter the number: "))
# if n % 2 == 1:
#     print("Odd")
# else:
#     print("Even")

# Nested if-else statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Childs tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif age >=45 and age <=55:
        print("Everything is going to be okay, have a free ride with us.")
    else:
        print("Adult tickets are $12")
        bill = 12

    wants_photos = input("Do you want a photo? Type y for yes or n for no: ")
    if wants_photos == 'y':
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you ride")



"""
Logical Operators are: and, or, not
"""

