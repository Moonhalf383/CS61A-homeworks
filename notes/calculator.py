def double(x):
    if isinstance(x,str):
        raise TypeError('double takes only numbers.')
    return x * 2 

def invert(x):
    result = 1/x 
    print('Never printed if x is 0.')
    return result 

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)


print(invert(3))
print(invert_safe(0))


def reduce(f,s,initial):
    """Conbine the elements of s using f start with initial.

    >>>reduce(mul, [2, 4, 8], 1)
    64
    >>>reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial,x)
    return initial

def truediv(x,y):
    return x/y 

def divide_all(n, ds):
    try:
        return reduce(truediv,ds,n)
    except ZeroDivisionError as e:
        return float('inf')
