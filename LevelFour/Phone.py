class Phone:
    phone_version = "S10"
    brand_version = "Samsung"
    user_name = ""
    phone_model = "S10+"

    def get_model(self):
        return self.phone_model
        # return "S10+"

    def set_model(self, value):
        self.phone_model = "S10+, " + value

    # Constructor
    def __init__(self, user_name):
        self.user_name = user_name

    def boot_logo(self):
        print("Samsung", self.phone_version)


john = Phone("John Phone")
john.phone_version = "iPhone 10 X Max"
john.set_model("iPhone")
print(john.get_model())
john.boot_logo()
