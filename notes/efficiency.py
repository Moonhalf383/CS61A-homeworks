def fib(n):
    if n == 0 or n == 1:
        return n 
    else:
        return(fib(n-1)+fib(n-2))

def count(f):
    def counted(n):
        counted.call_count += 1 
        return f(n)
    counted.call_count = 0
    return counted

fib = count(fib)
print(fib(5))
print(fib.call_count)
print(fib(30))
print(fib.call_count)

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

fib = count(fib)
counted_fib = fib
fib = memo(fib)
fib = count(fib)
print(fib(30))
print(fib.call_count)

def exp(b,n):
    if n == 0:
        return 1 
    else:
        return b * exp(b,n-1)

def exp_fast(b, n):
    if n == 0:
        return 1 
    elif n % 2 == 0:
        return square(exp_fast(b,n//2))
    else:
        return b * exp_fast(b,n-1)

def square(x):
    return x * x 

def count_frame(f):
    def counted(n):
        counted.open_count+=1 
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1 
        return result 
    counted.open_count = 0
    counted.max_count = 0
    return counted

fib = count_frame(fib)
print(fib(30))
print(fib.max_count)
