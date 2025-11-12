'Using Bulit-in Function.'

'Indices of elements that have the smallest absolute value.'
def indices_abs_smallest(l):
    assert isinstance(l,list) and l != []
    ans = []
    l = [abs(i) for i in l]
    for i in range(len(l)):
        if l[i] == min(l):
            ans.append(i)
    return ans 

print(indices_abs_smallest([1,2,3,4,5]))
print(indices_abs_smallest([4,3,-2,-1,7]))

'Largest sum of two adjacent elements.'
def largest_sum_adjacent(l):
    l = [l[i]+l[i+1] for i in range(len(l)-1)]
    return max(l)

print(largest_sum_adjacent([-4,-3,-2,3,2,4]))

'Dictionary mapping digit d to the elements end with d.'
def dict_map(l):
    ans_dict = {}
    for element in l:
        if element%10 not in ans_dict:
            ans_dict[element%10] = [element]
        else:
            ans_dict[element%10].append(element)
    return ans_dict

print(dict_map([5,8,13,21,34,55,89]))

'Does every element equal to some others?'
def element_equal(l):
    state = {}
    for element in l:
        if element not in state:
            state[element] = False 
        else:
            state[element] = True 
    return all(state.values())

print(element_equal([-4,-3,-2,3,2,4]))
print(element_equal([4,3,2,4,3,2]))

#######

def min_abs_indices(l):
    min_abs = min(map(abs,l))
    return [i for i in range(len(l)) if abs(l[i]) == min_abs]

def largest_adj_sum(l):
    return max([a + b for a,b in list(zip(l[:-1],l[1:]))])

def digit_dict(l):
    return {d : [x for x in l if x % 10 == d] for d in range(10) if any([x % 10 == d for x in l])}

def all_have_a_equal(l):
    return all([sum([1 for y in l if y == x])>1 for x in l])

########


class Link:
    empty = ()
    def __init__(self,first,rest = empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest 
    def __repr__(self):
        if self.rest:
            rest_repr = ', '+repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.rest)+rest_repr+')'
    def __str__(self):
        string = '< '
        while self is not Link.empty:
            string += str(self.first)+' '
            self = self.rest
        return string + '>'

def ordered(s, key = lambda x : x):
    if s == Link.empty or s.rest == Link.empty:
        return True 
    elif key(s.first) > key(s.rest.first):
        return False 
    else:
        return ordered(s.rest,key)

def merge(s, t):
    if s == Link.empty:
        return t 
    elif t == Link.empty:
        return s 
    elif s.first <= t.first:
        return Link(s.first,merge(s.rest,t))
    else:
        return Link(t.first,merge(s,t.rest))

def merge_in_place(s, t):
    if s == Link.empty:
        return t 
    elif t == Link.empty:
        return s 
    elif s.first <= t.first:
        #return Link(s.first,merge(s.rest,t))
        s.rest = merge_in_place(s.rest,t)
        return s 
    else:
        # return Link(t.first,merge(s,t.rest))
        t.rest = merge_in_place(s,t.rest)
        return t 
