number = 5
factorial_value = 1
if number < 0:
    print("We don't calculate negative factorials'")
elif number == 0:
    print("The result is 1")
else:
    for i in range(1, number + 1):
        factorial_value = factorial_value * i
    print("The result is ", factorial_value)