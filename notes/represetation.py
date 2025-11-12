'Representation'

s = 'Hello world!'

print(str(s))

print(repr(s))

print(repr(repr(repr(s))))

print(eval(eval(eval(repr(repr(repr(s)))))))

'F-String'

from math import pi 

print(f'Pi started with {pi}...')

def gcd(n, d):
    while n!=d:
        n,d = min(n,d),abs(n-d)
    return n 

class Ratio():
    def __init__(self,n,d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer,self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer,self.denom)
    
    def __add__(self,other):
        n = self.numer
        d = self.denom
        if isinstance(other,int):
            n = self.numer + other * self.denom
            d = self.denom
        elif isinstance(other,Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        g = gcd(n,d)
        return Ratio(n//g,d//g)
    __radd__ = __add__ 

    def __float__(self):
        return self.numer/self.denom

half = Ratio(1,2)
print()
print(half)
print(repr(half))
print()
print(Ratio(1,3)+Ratio(1,6))
print(repr(Ratio(1,3)+1))
print(Ratio(4,6)+2+Ratio(11,46))

print(0.22 + Ratio(123,567))
