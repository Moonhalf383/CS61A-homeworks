def count_while_version(s,value):
    total,index = 0,0
    while index < len(s):
        element = s[index]
        if element == value:
            total += 1
        index += 1
    return total

def count_for_version(s,value):
    total = 0
    for i in s:
        if i == value:
            total += 1
    return total

print(count_while_version([1,2,3,4,5,2,2,3],2))
print(count_for_version([1,2,3,4,5,2,2,3],2))

# Sequence unpacking in For statementt

pairs = [[1,2],[2,2],[3,1],[4,4]]
same_count = 0
for x,y in pairs:
    if x == y:
        same_count += 1

print(same_count)

print(list(range(-2,2)))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i 
    return total

print(sum_below(5))

letters = ['a','b','c','d','e','f','m','o','n']
print([letters[i] for i in [3,4,6,7]])

odd = [1,3,5,7,9]
print([x+1 for x in odd])
print([x for x in odd if 25 % x == 0])
print([x+1 for x in odd if 25 % x == 0])

def divisor(x):
    return [1] + [n for n in range(2,x) if x%n == 0]

print(divisor(4))
print(divisor(78))




    
