class Account:
    def __init__(self,account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            return 'Insufficient funds.'
        self.balance -= amount
        return self.balance

a = Account('John')
print(a.holder)
print(a.balance)
print(a.deposit(10))
print(a.withdraw(5))
print(a.balance)
