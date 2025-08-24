# test.py
# def greet(name):
#     return f"Hello, {name}! Welcome to GitHub."

# print(greet("Pritish"))
#
#constructor
class Atm :
    def __init__(self) :
        self.pin = "1234"
        self.balance=123456
        self.menu()
    def menu(self):
        r=self.pin
        s=self.balance
        print(r)
        print(s)
k=Atm()