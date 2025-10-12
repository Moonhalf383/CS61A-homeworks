def print_sums(x):
	print(x)
	def next_sum(y):
		return print_sums(x+y)
	return next_sum
	
print_sums(1)(3)(5)

def split(n):
	x,y = n//10,n%10
	return x,y
	
def sum_digits(x):
	if x < 10:
		return x
	all_but_last,last = split(x)
	return sum_digits(all_but_last)+last
	
print(sum_digits(12345))

#luhn algorithm

def luhn_algorithm(x):
    if x<10:
        return x
    all_but_last,last = split(x)
    return luhn_algorithm_double(all_but_last)+last

def luhn_algorithm_double(x):
    if x<10:
        return sum_digits(x*2)
    all_but_last,last = split(x)
    return luhn_algorithm(all_but_last)+sum_digits(last*2)

print(luhn_algorithm(5105105105105100))

def sum_digits_iter(x):
    digit_sum = 0
    while x>0:
        x,last = split(x)
        digit_sum+=last
    return digit_sum

print(sum_digits_iter(12345))
