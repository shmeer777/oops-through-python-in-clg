class neo:
    def __init__(self):
        self.balance=0
        print("welcome to NEO")
    def deposit(self):
        amount=float(input("enter deposit amount:"))
        self.balance+= amount
        print("\nAmount deposited:",amount)
    def withdraw(self):
        amount=float(input("enter amount to be withdrawn:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n you withdrew:",amount)
        else:
            print("\n Insufficient balance")
    def display(self):
        print("\n Available balance=",self.balance)
        
#driver code        
s=neo()
s.deposit()
s.withdraw()
s.display()
