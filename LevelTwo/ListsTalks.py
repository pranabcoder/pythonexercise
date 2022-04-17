marvelHero = ["Spiderman", "Ironman", "Thor"]
dcHero = ["Batman", "Flash", "Aquaman", "Batman"]

# print(dcHero[1:])

# del dcHero[1]
# print(dcHero)
del dcHero[1]
# dcHero[1] = "Flash"
dcHero.append("Flash")
dcHero.insert(0, "Green Arrows")
# print(dcHero)
dcHero.remove("Flash")
# print(dcHero)
dcHero.reverse()
# print(dcHero)
print(dcHero.count("Batman"))
print(dcHero + marvelHero)
