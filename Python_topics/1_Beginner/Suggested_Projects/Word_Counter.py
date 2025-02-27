from pathlib import Path

def word_counter(text, word):
    with open(Path(f"{text}.txt"), "r") as file:
        content = file.read().upper()
    print(content)
    print(content.count(word.upper()))

text = input("What text file: ")
word = input("What word: ")
print(Path(f"{text}.txt"))
word_counter(text, word)
