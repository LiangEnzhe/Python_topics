from pathlib import Path
import json

def todo():
    global todolist
    print("1. Display all")
    print("2. Add")
    print("3. Remove")
    print("4. Exit\n")
    while True:
        choice = input("What to do?: ")
        if choice == "1":
            number = 1
            for i in todolist:
                print(f"{number}. {i}\n")
                number += 1
        elif choice == "2":
            task = input("What to add: ")
            if task not in todolist:
                todolist.append(task)
            else:
                print("already there")
            with open(Path("Task.json"), "w", encoding="utf-8") as f:
                json.dump(todolist, f, ensure_ascii=False, indent=4)
            print(f"{task} added")
        elif choice == "3":
            task = input("What to remove: ")
            if task in todolist:
                todolist.pop(todolist.index(task))
                with open(Path("Task.json"), "w", encoding="utf-8") as f:
                    json.dump(todolist, f, ensure_ascii=False, indent=4)
                print(f"{task} removed")
            else:
                print("already not there")
        elif choice == "4":
            quit()
        else:
            print("type smth normal")

with open(Path("Task.json"), "r", encoding="utf-8") as f:
    todolist = json.load(f)

todo()
