import random

random_choice = random.randint(0, 2)
if random_choice == 0:
    computer = "Камень"
elif random_choice == 1:
    computer = "Бумага"
else:
    computer = "Ножницы"

user = input("камень, ножницы, бумага?")
print("Вы выбрали", user + ", компьютер выбрал", computer)
winner = " "
if computer == user:
    winner = "Ничья"
    print(winner)
else:
    if computer == "Камень" and user == "Ножницы":
        winner = "Компьютер"
    elif computer == "Бумага" and user == "Камень":
        winner = "Компьютер"
    elif computer == "Ножницы" and user == "Бумага":
        winner = "Компьютер"
    else:
        winner = "Вы победили"
    print(winner)
