class Samsung:

    def __init__(self):
        print(" I am Samsung")

    def make_screen(self):
        print("I make screens from :Samsung")

    def test_screen(self):
        print("Screen test 1: OK")
        print("Screen test 2: OK")
        print("Screen test 3: OK")


class Iphone(Samsung):

    def __init__(self):
        print("I am Iphone")
        # super().__init__()

    def a3_chips(self):
        print("I make A3 bionic chips")

    def iPhone_test(self):
        print("A3 test: OK")
        # super().test_screen()

    def make_screen(self):
        # super().make_screen()
        print("I make screens : Apple")


user = Iphone()
user.a3_chips()
user.make_screen()
user.iPhone_test()
user.make_screen()
