# ----------------------------------------------------------------------
# If-else Conditions
# ----------------------------------------------------------------------
# If-else conditions allow decision-making in Python based on a condition.
# Syntax:
# if condition:
#     # Code to execute if condition is True
# elif another_condition:
#     # Code to execute if another_condition is True
# else:
#     # Code to execute if all conditions are False

# Example:
age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")  # Prints this because age is 20
else:
    print("You are a senior citizen.")

# Nested if-else: You can place if-else statements inside another if-else.
score = 85
if score >= 90:
    print("Grade: A")
else:
    if score >= 80:
        print("Grade: B")  # Prints this because score is 85
    else:
        print("Grade: C")

# ----------------------------------------------------------------------
# Logical Operators (and, or, not)
# ----------------------------------------------------------------------
# Logical operators are used to combine conditions.

# 1. 'and': Returns True if both conditions are True.
x = 5
y = 10
if x > 0 and y > 0:
    print("Both numbers are positive.")  # Prints this

# 2. 'or': Returns True if at least one condition is True.
if x > 0 or y < 0:
    print("At least one number is positive.")  # Prints this

# 3. 'not': Reverses the condition's result.
if not x < 0:
    print("x is not negative.")  # Prints this

# ----------------------------------------------------------------------
# Loops (for, while)
# ----------------------------------------------------------------------

# Loops are used to execute a block of code repeatedly.

# 1. For Loop:
# A 'for' loop iterates over a sequence (like a list, string, or range).

# Example: Iterating over a range of numbers
for i in range(5):  # range(5) generates numbers from 0 to 4
    print(i)  # Prints: 0, 1, 2, 3, 4

# Example: Iterating over a string
word = "Python"
for char in word:
    print(char)  # Prints each character of the word

# 2. While Loop:
# A 'while' loop continues as long as a condition is True.

# Example:
count = 0
while count < 5:  # Executes as long as count is less than 5
    print(count)  # Prints: 0, 1, 2, 3, 4
    count += 1  # Increment count to avoid an infinite loop

# ----------------------------------------------------------------------
# Loop Control (break, continue, else with loops)
# ----------------------------------------------------------------------

# 1. 'break': Exit the loop prematurely when a condition is met.
for num in range(10):
    if num == 5:  # Stop the loop when num is 5
        break
    print(num)  # Prints: 0, 1, 2, 3, 4

# 2. 'continue': Skip the current iteration and move to the next one.
for num in range(10):
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num)  # Prints: 1, 3, 5, 7, 9

# 3. 'else' with Loops:
# The 'else' block runs if the loop completes without hitting a 'break'.
for num in range(5):
    print(num)
else:
    print("Loop completed successfully!")  # Prints this if the loop isn't terminated by 'break'

# Example where 'break' prevents the 'else' block:
for num in range(5):
    if num == 3:
        break
    print(num)
else:
    print("This won't print because the loop was interrupted.")

# ----------------------------------------------------------------------
# match-case
# ----------------------------------------------------------------------

# Python match-case Explained (Introduced in Python 3.10)

# The match-case statement is similar to switch-case in other languages.
# It allows pattern matching, making conditional checks more readable.

# Basic Usage of match-case
def check_status(code):
    match code:  # Match the variable 'code' against different cases
        case 200:
            return "OK"  # Case when code is 200
        case 400:
            return "Bad Request"  # Case when code is 400
        case 404:
            return "Not Found"  # Case when code is 404
        case 500:
            return "Internal Server Error"  # Case when code is 500
        case _:  # Default case (like 'else' in if-else)
            return "Unknown Status Code"

print(check_status(200))  # Output: OK
print(check_status(404))  # Output: Not Found
print(check_status(999))  # Output: Unknown Status Code

# Using match-case with Multiple Conditions
def get_animal_sound(animal):
    match animal:
        case "dog" | "wolf":  # Multiple matches for the same case
            return "Bark"
        case "cat":
            return "Meow"
        case "cow":
            return "Moo"
        case _:
            return "Unknown Sound"

print(get_animal_sound("dog"))  # Output: Bark
print(get_animal_sound("cat"))  # Output: Meow
print(get_animal_sound("lion"))  # Output: Unknown Sound

# Using match-case with Structured Patterns (Tuples)
def point_location(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):  # Matches any (x, 0) where y is 0
            return f"On the X-axis at {x}"
        case (0, y):  # Matches any (0, y) where x is 0
            return f"On the Y-axis at {y}"
        case (x, y):
            return f"In the plane at ({x}, {y})"
        case _:
            return "Unknown location"

print(point_location((0, 0)))  # Output: Origin
print(point_location((5, 0)))  # Output: On the X-axis at 5
print(point_location((0, 7)))  # Output: On the Y-axis at 7
print(point_location((3, 4)))  # Output: In the plane at (3, 4)


# Using match-case with Dictionaries (Unpacking)
def user_info(user):
    match user:
        case {"name": name, "age": age}:  # Unpacks dictionary keys
            return f"User {name} is {age} years old"
        case _:
            return "Invalid user data"

print(user_info({"name": "Alice", "age": 25}))  # Output: User Alice is 25 years old
print(user_info({"name": "Bob"}))  # Output: Invalid user data
