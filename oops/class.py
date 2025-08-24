
#software for an ATM machine :
class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        user_input =int( input("""
                           Hello how would you like to proceed ?
                           1.for create pin
                           2.for deposit
                           3.for withdraw
                           4.check balance
                           5.exit
                           """))
        if user_input == 1:
            self.create_pin()
            
        elif user_input==2:
            self.deposit()
        elif user_input == 3:
            self.withdraw_money()
        elif user_input == 4 :
            self.check_balance()
        elif user_input == 5:
            print("thank you")
        
    def create_pin(self):
        self.pin = input("Enter your pin:  ")
        print("Pin set")
        self.menu()
    def deposit(self):
        u_input = input("enter your pin:   ")
        if u_input == self.pin :
            deposited_money = int(input("enter the value you want to deposit : "))
            self.balance = deposited_money + self.balance
            print("your amount is deposited")
        else:
            print("incorrect pin")
            self.menu()
        self.menu()
    def withdraw_money(self):
         u_input = input("enter your pin:   ")
         if u_input == self.pin :
            withdrawn_money = int(input("enter money you want to withdraw"))
            self.balance = self.balance - withdrawn_money
            print("money withdrawn successfully")
         else:
             print("incorrect pin")
             self.menu()
         self.menu()
    def check_balance(self):
         u_input = input("enter your pin:  ")
         if u_input == self.pin :
          print(f"your balance is : {self.balance}")
         else:
             print("incorrect pin")
             self.menu()
         self.menu()
    def exit(self):
        print("thank you")



















k = Atm()
k.withdraw_money()