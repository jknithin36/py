class Bank:
    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} . New Balance : ${self.balance}")
        else:
            print("Amount must be Postive")

    
    def withdraw(self, amount):
        if amount < self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Succefully withdrawn, Balanace: ${self.balance}")
    
    def check_balance(self):
        print(f"{self.owner}'s current balance : ${self.balance}")

    


Account1 = Bank("nithin")
Account2 = Bank("Shiva")

Account1.check_balance()
Account1.deposit(1000)
Account1.check_balance()

    



        