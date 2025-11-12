def evens(start,end):
    even = start + start % 2
    while even < end:
        yield even
        even += 2
it = evens(1,10)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

'A yield from statement can yield all value from an iterator or an iterable'

def a_then_b(a,b):
    for x in a:
        yield x
    for x in b:
        yield x 

def a_then_b_yieldfrom(a,b):
    yield from a 
    yield from b 
print()        
print(list(a_then_b([3,4],[5,6])))
print(list(a_then_b_yieldfrom([3,4],[5,6])))

'countdown function itself is a generator,return a iterator'
'yield from statement means next time the output iterator is called through next,it will yield data from another iterator.'
def countdown(x):    
    if x > 0:
        yield x 
        yield from countdown(x-1) 
    else:
        yield 'Blast off!'
print()
x = countdown(3)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s 
print()
print(list(prefixes('test')))

def substring(s):
    if s:
        yield from prefixes(s)
        yield from substring(s[1:])

print()
print(list(substring('test')))

def list_partitions(n,m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partitions(n-m,m)]
        without_m = [p for p in list_partitions(n,m-1)]
        return with_m + without_m + exact_match

print(list_partitions(6,4))     

def partitions(n,m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partitions(n-m,m)]
        without_m = partitions(n,m-1) 
        return with_m + without_m + exact_match

for p in partitions(6,4):
    print(p)

print('generator version:')
def partitions_yield(n,m):
    if n>0 and m>0:
        if n == m:
            yield str(m)
        for p in partitions(n-m,m):
            yield p + ' + ' + str(m)
        yield from partitions_yield(n,m-1)

for p in list(partitions_yield(6,4)):
    print(p)

