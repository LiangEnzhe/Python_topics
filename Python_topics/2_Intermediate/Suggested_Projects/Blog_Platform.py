import json
from pathlib import Path

with open(Path("blog_posts.json"), "r+", encoding="utf-8") as f:
    words = json.load(f)
    
def save_posts():
    with open(Path("blog_posts.json"), "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=4)
            
def view_post():
    print("\n")
    for index, match in enumerate(words, 1):
        print("----------------------------------------")
        print(f"{index}. " + match["title"])
        print(match["content"])
    print("----------------------------------------\n")


def create_post():
    title = input("Title: ")
    content = input("Content: ")
    dictionary = {"title": title, "content": content}
    words.append(dictionary)

def update_post():
    index = int(input("What post to change: ")) - 1
    try:
        item = input("What to change; title or content: ")
        dic = words[index]
        if item.__eq__("title"):
            dic["title"] = input("Text: ")
        else:
            dic["content"] = input("Text: ")
    except:
        print("No such post")
        
def delete_post():
    index = int(input("What post to change: ")) - 1
    del words[index]
    
def main():
    while True:
        print("1. View ALL Posts")
        print("2. Create Post")
        print("3. Update Post")
        print("4. Delete Post")
        print("5. Stop")
        choice = int(input("Enter nunmber: "))
        match choice:
            case 1:
                view_post()
            case 2:
                create_post()
                save_posts()
            case 3:
                update_post()
                save_posts()
            case 4:
                delete_post()
                save_posts()
            case 5:
                break
    
main()
