import re
from pathlib import Path

def search_file(text, pattern):
    try:
        with open(Path(f"{text}.txt"), "r") as file:
            content = file.read()
            return re.findall(pattern, content)
    except:
        print("Write normal name")
        main()

def display_matches(matches):
    if matches:
        print("Matches found:\n")
        for index, match in enumerate(matches, 1):
            print(f"{index}. {match}")
    else:
        print("No matches found.")
    
def main():
    text = input("Name: ")
    print("1. email\n")
    print("2. telephone number\n")
    print("3. custom")    
    choice = input("What to choose: ")

    if choice == "email":
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    elif choice == "telephone number":
        pattern = r"\b\d{10}\b"
    elif choice == "custom":
        pattern = input("Enter your custom regex pattern: ").strip()
    else:
        print("Invalid. kys")

    display_matches(search_file(text, pattern))
    
main()
