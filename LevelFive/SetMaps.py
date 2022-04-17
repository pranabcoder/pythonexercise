super_hero = (1, 2, 3, 4)

print(super_hero)


def get_square(num):
    return num * num


result = map(get_square, super_hero)
result_two = set(result)
print(result_two)
