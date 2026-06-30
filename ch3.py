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
