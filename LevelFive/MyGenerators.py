import random

super_hero = ["Batman", "Hulk", "Thor"]

# for h in super_hero:
#     print(h)


def magic():
    for i in range(6):
        yield random.randint(1, 20)


for number in magic():
    print("Value is ", number)
