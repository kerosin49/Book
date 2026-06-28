print("what is name your dog?")
dog_name = input()
print(dog_name, "good name")

print("how old your dog?")
dog_age = int(input())
print(dog_age * 7)

print("how weight pounds", dog_name, sep=" ", end="?")
weight = int(input())
print(weight)

print(weight, "need convert pounds to kilograms")
kg = weight * 0.454
print(kg)

print("now let's find out the averega value")
avg = kg / 3
print(avg)
