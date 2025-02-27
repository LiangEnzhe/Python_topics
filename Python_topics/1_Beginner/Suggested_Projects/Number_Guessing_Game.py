import random

def guess():
    global minimum, maximum
    answer = input("Guess the number: ")
    correct = random.randrange(minimum, maximum + 1)
    if answer.__eq__(str(correct)):
        print(f"GOODMF, it is {answer}")
    elif answer.__eq__("change"):
        minimum = int(input("MIN: "))
        maximum = int(input("MIN: "))
    elif answer.__eq__("quit"):
        quit()
    else:
        print(f"kys, it is {correct}")
            
minimum = int(input("MIN: "))
maximum = int(input("MIN: "))
loop = True

while loop:
    guess()
