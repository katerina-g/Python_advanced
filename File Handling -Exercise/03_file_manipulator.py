import os

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    elif command[0] == "Create":
        file_name = command[1]
        with open(file_name, "w") as file:
            file.write("")
    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]
        with open(file_name, "a") as file:
            file.write(content + "\n")
    elif command[0] == "Replace":
        file_name = command[1]
        old_content = command[2]
        new_content = command[3]
        if os.path.exists(file_name):
            with open(file_name, "r+") as file:
                text = file.read()
            text = text.replace(old_content, new_content)
            with open(file_name, "w") as file:
                file.write(text)
        else:
            print("An error occurred")
    elif command[0] == "Delete":
        file_name = command[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
