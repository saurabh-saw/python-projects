# Subscripting
print("Hello"[0])

# String
print("123" + "456")

# Integers
print(123 + 456)

# Large Numbers
print(123_456_789)

# FLoat
print(3.14159)

# Boolean
print(True)
print(False)

# Type Checking
print(type(123))
print(type("abc"))
print(type(3.14159))
print(type(True))

# Type Conversion
print(int("123") + int("456"))
print(bool(123))
"""
int(), str(), float(), bool()
"""

# Mathematical Operations
print(123 + 345)
print(40 - 30)
print(2 * 3)
print(5 / 2) # implicit type conversion to float
print(5 // 2)
print(2 ** 8)

"""
Operator importances: PEMDASLR
(), **, */ , +- 
Left to right for same importance
"""

print(3 * 3 + 3 / 3 - 3) # 7

# Number Manipulation
pos = 3.5
neg = -3.5

# It floor towards 0
print(int(pos)) # 3
print(int(neg)) # -3

# It rounds towards nearest integer
print(round(pos)) # 4
print(round(neg)) # -4

# Round to a certain digit
print(round(3.14159, 2)) # 3.14

# Assignment
# pos = pos + neg
pos += neg
print(pos)

# f-string for combining different data types
score = 0
height = 1.8
winning = True
print(f"Your score is {score}, your height is {height}, you are {winning}")