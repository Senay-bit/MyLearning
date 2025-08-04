listofShame = []

while True:
    question = input("Add or remove?\n> ").strip().lower()
    if question == "add":
        name = input("What's your name?\n> ").strip().lower().capitalize()
        age = input("What is your age?\n> ").strip()
        pref = input("What's your computer platform>\n> ").strip().lower().capitalize()
        row = [name, age, pref]
        listofShame.append(row)
    else:
        item = input("What's the name of the person you would like to remove?\n> ").strip().lower().capitalize()
        for i in listofShame:
            if item in i:
                listofShame.remove(i)

    print()
    exit = input("Exit? y/n\n> ").strip().lower()
    print()
    if exit == "y":
        break

for i in listofShame:
    for k in i:
        print(f"{k:^10} | ", end = "")
    print()