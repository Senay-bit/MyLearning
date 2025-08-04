import os, time

TodoList = []

def view():
    period = (len(TodoList) * 2) - 3
    if period < 1:
        period = 1
    elif period > 10:
        period = 10
    for i in TodoList:
        for k in i:
            print(f"{k:^15} | ", end = "")
        print()
    time.sleep(period)

while True:
    print("TO-DO List Management System")
    print()
    print("1. Add\n2. Remove\n3. Edit\n4. View\n5. Exit")
    print()
    try:
        question = int(input("> ").strip())
    except ValueError:
        print("Please specify what you wish to do using the numbers corresponding to your desired action.")
        time.sleep(3)
        os.system("clear")
        continue
    os.system("clear")

    if question == 1:
        print("ADD")
        print()
        item = input("What is it?\n> ").strip().lower().capitalize()
        day = input("When is it?\n> ").strip().lower().capitalize()
        priority = input("How important is it? high/medium/low\n> ").strip().lower().capitalize()
        print()
        profile = [item, day, priority]
        if profile not in TodoList:
            TodoList.append(profile)
            print("Task has been added!")
        else:
            print("Task is already in your To-do list.")
    while question == 2:
        print("REMOVE")
        print()
        item = input("What's the task you want to remove?\n> ").strip().lower().capitalize()
        print()
        deleted = False
        for i in TodoList:
            for k in i:
                if k == item:
                    TodoList.remove(i)
                    print("Task has been removed!")
                    deleted = True
        if deleted == False:
            exit = input("Sorry, couldn't find the task you want to remove. Exit? y/n\n> ").strip().lower()
            if exit == "y":
                break
            elif exit == "n":
                os.system("clear")
                continue
        else:
            break
    while question == 3:
        print("EDIT")
        print()
        group = input("What task do you want to edit?\n> ").strip().lower().capitalize()
        item = input("What do you want to edit in that task? (Task, Day, Importance)\n> ").strip().lower().capitalize()
        change = input("What do you want to change it into?\n> ").strip().lower().capitalize()
        print()
        error = False
        if item == "Task":
            pos = 0
        elif item == "Day":
            pos = 1
        elif item == "importance":
            pos = 2
        else:
            print()
            print('Please answer the question using "Task", "Day", or "Importance"')
            time.sleep(3)
            os.system("clear")
            continue
        for i in TodoList:
            for k in i:
                if k == group:
                    error = True
                    x = TodoList.index(i)
                    for l in i:
                        TodoList[x][pos] = change
        if error:
            print(f"{group} has been succesfully changed into {change}")
            break
        else:
            exit = input(f"Sorry, {group} is not in the To-do List. Exit? y/n\n> ").strip().lower()
            if exit == "y":
                break
            elif exit == "n":
                os.system("clear")
                continue
    while question == 4:
        print("VIEW")
        print()
        items = input("Do you want to view high priority tasks only or all tasks? priority/all\n> ").strip().lower()
        print()
        if items == "priority":
            for i in TodoList:
                for k in i:
                    if k == "High":
                        for l in i:
                            print(f"{l:^15}", end = " | ")
                        print()
            time.sleep(5)
            break
        elif items == "all":
            view()
            break
        else:
            print("Please specify if you wish to view priority tasks or all tasks.")
            time.sleep(3)
            os.system("clear")
            continue
    if question == 5:
        exit = input("Are you sure you want to exit? y/n\n> ").strip().lower()
        if exit == "y":
            os.system("clear")
            break
        else:
            os.system("clear")
            continue
    if question > 5:
        print("Please input the numbers corresponding to the task you want to perform only.")
    time.sleep(3)
    os.system("clear")
print("FINSHED TO-DO LIST")
print()
view()
input("")