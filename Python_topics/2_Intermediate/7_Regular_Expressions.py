# ----------------------------------------------------------------------
# Regular Expressions (RegEx) with the `re` Module
# ----------------------------------------------------------------------
# Regular expressions allow you to search, match, and manipulate strings
# based on specific patterns.

import re  # Import the `re` module

# ----------------------------------------------------------------------
# 1. Pattern Matching Basics
# ----------------------------------------------------------------------
# A regular expression is a pattern describing a set of strings.
# Common symbols:
# - `.`  : Matches any character except a newline.
# - `^`  : Matches the start of a string.
# - `$`  : Matches the end of a string.
# - `*`  : Matches zero or more occurrences of the preceding character.
# - `+`  : Matches one or more occurrences of the preceding character.
# - `?`  : Matches zero or one occurrence of the preceding character.
# - `{}` : Specifies the number of occurrences (e.g., `{2}` matches exactly 2).
# - `[]` : Matches any character inside the brackets.
# - `|`  : Acts as "or" (e.g., `a|b` matches "a" or "b").
# - `\d` : Matches any digit (0-9).
# - `\w` : Matches any word character (letters, digits, underscore).
# - `\s` : Matches any whitespace character (spaces, tabs, etc.).

# Example: Basic pattern matching
pattern = r"\d+"  # Matches one or more digits
text = "There are 42 apples and 7 oranges."
matches = re.findall(pattern, text)  # Find all matches in the text
print(matches)  # Prints: ['42', '7']

# ----------------------------------------------------------------------
# 2. Search and Match Operations
# ----------------------------------------------------------------------

# a. re.search(): Searches for the first match of the pattern in the string.
# Returns a match object if found, otherwise None.
text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"  # Pattern for a phone number
match = re.search(pattern, text)
if match:
    print("Found:", match.group())  # Prints: Found: 123-456-7890
else:
    print("No match found.")

# b. re.match(): Checks for a match at the beginning of the string only.
pattern = r"My phone number"  # Pattern for the start of the text
match = re.match(pattern, text)
if match:
    print("Match found at the start of the string.")  # Prints this
else:
    print("No match at the start.")

# ----------------------------------------------------------------------
# 3. Finding All Matches
# ----------------------------------------------------------------------
# re.findall(): Finds all matches of a pattern in the string and returns a list.

text = "Emails: alice@example.com, bob@gmail.com"
pattern = r"\w+@\w+\.\w+"  # Pattern for email addresses
matches = re.findall(pattern, text)
print(matches)  # Prints: ['alice@example.com', 'bob@gmail.com']

# ----------------------------------------------------------------------
# 4. Replace Operations
# ----------------------------------------------------------------------
# re.sub(): Replaces occurrences of the pattern with a specified string.

text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"  # Pattern for a phone number
replacement = "[REDACTED]"  # Replace the phone number
result = re.sub(pattern, replacement, text)
print(result)  # Prints: My phone number is [REDACTED].

# ----------------------------------------------------------------------
# 5. Advanced Examples
# ----------------------------------------------------------------------

# a. Extracting groups with re.search() and match.group()
text = "Order ID: #12345, placed on 2023-12-01."
pattern = r"#(\d+), placed on (\d{4}-\d{2}-\d{2})"  # Capture order ID and date
match = re.search(pattern, text)
if match:
    order_id = match.group(1)  # First captured group
    date = match.group(2)  # Second captured group
    print(f"Order ID: {order_id}, Date: {date}")  # Prints: Order ID: 12345, Date: 2023-12-01

# b. Compiling regular expressions for reuse
compiled_pattern = re.compile(r"\d{4}")  # Matches 4-digit sequences
matches = compiled_pattern.findall("2023 was a great year, 2024 will be better!")
print(matches)  # Prints: ['2023', '2024']

# c. Matching with flags (e.g., case-insensitive matching)
text = "Python is FUN!"
pattern = r"python"
match = re.search(pattern, text, re.IGNORECASE)  # Ignore case sensitivity
if match:
    print("Case-insensitive match found.")  # Prints this

# ----------------------------------------------------------------------
# Best Practices with Regular Expressions
# ----------------------------------------------------------------------
# 1. Use raw strings (r"pattern") to avoid escaping backslashes.
#    - Example: r"\d" is better than "\\d".
# 2. Compile regular expressions for complex patterns used multiple times.
# 3. Use descriptive variable names for patterns and results.
# 4. Use `match.group()` to extract matched groups when needed.
# 5. Avoid overly complex patterns; break them into simpler ones for clarity.
