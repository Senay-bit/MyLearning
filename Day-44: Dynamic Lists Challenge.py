import os, random, time

def num():
    number = random.randint(1, 100)
    return number

numbers = []
while len(numbers) < 8:
    values = num()
    if values not in numbers:
        numbers.append(values)

while True:
    print(f"{numbers[0]:^7} | {numbers[1]:^7} | {numbers[2]:^7}")
    print("--------------------------")
    print(f"{numbers[3]:^7} | {"BINGO":^7} | {numbers[4]:^7}")
    print("--------------------------")
    print(f"{numbers[5]:^7} | {numbers[6]:^7} | {numbers[7]:^7}")
    print()

    try:
        answer = int(input("What number was called?\n> ").strip())
        for i in range(len(numbers)):
            if answer == numbers[i]:
                numbers[i] = "x"
    except ValueError:
        print("Error. Please type in a proper number.")
        time.sleep(1)
    os.system("clear")
    win = True
    for i in numbers:
        if i != "x":
            win = False
    if win:
        break

print()
print("Bingo! You won!!")
input()