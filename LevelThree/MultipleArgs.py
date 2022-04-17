# def add_me(num_one, num_two):
#     total = num_one + num_two
#     return total
#
#
# # my_result = add_me(3, 5)
# print(add_me(3, 5))

# def add_me(*num):
#     total = 0
#     for v in num:
#         total = total + v
#     return total
#
#
# print(add_me(3, 5, 67, 8))

# def price_calculation(*prices):
#     price = sorted(prices, reverse=True)
#     total_one = price[0]
#     total = 0
#     for v in price:
#         total = total_one - v
#     return total
#
#
# print(price_calculation(100, 200))
import total as total


def price_calculation(*prices):
    price_count = len(prices)
    if price_count == 2:
        price = sorted(prices, reverse=True)
        total_one = price[0]
        result = 0
        for v in price:
            result = total_one - v
        return result
    else:
        print("Please enter two numbers")
        return


print(price_calculation(100, 300))
