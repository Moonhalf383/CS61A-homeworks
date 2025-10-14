odds = [3,5,7,9,11]
print([odds[i] for i in range(1,3)])
print(odds[1:3])
print(odds[:3])
print(odds[1:])
print(sum([2,3,4]))
print(sum([[2,3],[4]],[])) # the second parameter is the starting value,determine the type of tht expression.
# the default start value is zero,which cannot be added to a list
print([]+[2,3,4]+[5])

print (min(range(-5,6),key = lambda x:x*x))
"key expression determines the rule of the min function.In this example,it means to choose the x that present the lowest x square value."



print([x<5 for x in range(5)])

print(all([x<5 for x in range(5)]))

print(any([x<3 for x in range(5)]))

print('here' in 'where')

numerals = {'I':1,"V":5,"X":10}
print(numerals['X'])

print()

print(list(numerals))

print(numerals.values())

print(sum(numerals.values()))

print(list(numerals.values()))

d = {x*x:x for x in range (1,6) if x >2}
print(d)

def index(keys,values,match):
    return {k:[v for v in values if match(k,v)] for k in keys}

keys = [7,9,11]
values = range(30,50)
match = lambda k,v:v%k == 0

print()
print(index(keys,values,match))


