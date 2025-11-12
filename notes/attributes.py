class Account:
    insterest = 0.02
    def __init__(self,account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self,amount):
        self.balance += amount
        return self.balance

tom_account = Account('tom')
print(tom_account.insterest)
'Class attributes are shared among all its instances.'
print()
print(getattr(tom_account,'insterest'))
print(hasattr(tom_account,'insterest'))

Account.insterest = 0.04
print(getattr(tom_account,'insterest'))
'Class attribute assignment statement can change the attribute of all its instances'
'except for the special cases.'
tom_account.insterest = 0.08
Account.insterest = 0.05
print(tom_account.insterest)
'tom\'s insterest didnt change, since it was assigned specially.'

print()
a = Account('Alan')
f = a.deposit
print(f(10))
print(f(20))

print()
b = Account('Ada')
m = map(b.deposit,range(10,30))
print(next(m))
print(next(m))
print(next(m))

