import MyModuleTest
# val = MyModuleTest.add_me(5, 4)
# print(MyModuleTest.add_me(5, 4))
# print(add_me(20, 50))
from MyModuleTest import *


print("---------Welcome To Calculator---------")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
menu_value = int(input("Enter the Value between 1 to 4:"))
if menu_value == 1:
    values = take_user_data()
    print(add_me(values[0], values[1]))
elif menu_value == 2:
    values = take_user_data()
    print(sub_me(values[0], values[1]))
elif menu_value == 3:
    values = take_user_data()
    print(multiply_me(values[0], values[1]))
elif menu_value == 4:
    values = take_user_data()
    print(divide_me(values[0], values[1]))
else:
    print("Invalid Input !!! Please enter values between 1 to 4")
