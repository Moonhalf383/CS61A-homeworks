d = {'one':1,'two':2,'three':3}
d['zero'] = 0
k = iter(d.keys())
print(next(k))
print(next(k))
print(next(k))
print(next(k))
v = iter(d.values())
print(next(v))
print(next(v))
print(next(v))
print(next(v))
i = iter(d.items())
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print()

bcd = ['b','c','d']
print([x.upper() for x in bcd])
m = map(lambda x : x.upper(),bcd)
print(next(m))
print(next(m))
print(next(m))

def double(x):
    print('**', x, '=>', 2*x, '**')
    return 2*x 

m = map(double,range(3,7))
'map is a iterator, t is a iterator as well.When t is called through next,t will iteate m until m return a qualified number.'
f = lambda y : y >= 10
t = filter(f,m)
print(next(t))

print()

print(list(zip([1,2],[3,4])))
print(list(zip([1,2],[3,4],[5,6,7])))

def palindrome(s):
    return all([a == b for a, b in zip(s,reversed(s))])

print(palindrome([1,2,3,2,1]))
print(palindrome([1,2,3,4,5]))
