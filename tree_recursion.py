def cascade(x):
    if x < 10:
        print(x)
    else:
        print(x)
        cascade(x//10)
        print(x)

#cascade(12345)

def inverse_cascade(x):
    grow(x)
    print(x)
    shrink(x)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n:f_then_g(grow,print,n//10)
shrink = lambda n:f_then_g(print,shrink,n//10)

inverse_cascade(12345)

print()

def count_partitions(x,n):
    if x == 2 or x == 1:
        return 1
    ans = 0
    if x<=n:
        for i in range(x-1):
            ans+=count_partitions(i,n)
        return ans
    for i in range(n):
        ans += count_partitions(x-i-1,n)
    return ans

print(count_partitions(6,4))

def count_partitions_cs61a(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions_cs61a(n-m,m)
        without_m = count_partitions_cs61a(n,m-1)
        return with_m + without_m

print(count_partitions_cs61a(6,4))


