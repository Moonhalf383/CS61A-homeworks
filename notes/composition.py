from re import L
from typing import Self


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

def range_link(start,end):
    if start >= end:
        return Link.empty
    else:
        return Link(start,range_link(start+1,end))

def map_link(f,s):
    if s is Link.empty:
        return s 
    else:
        return Link(f(s.first),map_link(f,s.rest))

def filter_link(f, s):
    if s is Link.empty:
        return s 
    filtered_rest = filter_link(f,s.rest)
    if f(s.first):
        return Link(s.first,filtered_rest)
    else:
        return filtered_rest

def add(s,v):
    if s.first > v:
        s.first,s.rest = v,Link(s.first,s.rest) 
    elif s.first < v and s.rest == Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        s.rest = add(s.rest,v)
    return s 

test_link = Link(3,Link(4,Link(5)))
print(test_link)
print(test_link.first)
print(test_link.rest.first)
print(test_link.rest.rest.first)
print(range_link(1,6))
print(map_link(lambda x : x * x,range_link(1,6)))
print(filter_link(lambda x : x % 2 == 1,map_link(lambda x : x * x,range_link(1,6))))

class Tree:
    def __init__(self, label, branches = []):
        self.label = label 
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branches = list(branches)
    def __repr__(self):
        branch_str = ''
        if self.branches:
            branch_str = ', '+repr(self.branches)
        else:
            branch_str = ''
        return 'Tree{0}{1}'.format(repr(self.label),branch_str)
    def __str__(self):
        return '\n'.join(self.indented())
    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('   '+line)
        return [str(self.label)] + lines
    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left_tree = fib_tree(n-1)
        right_tree = fib_tree(n-2)
        fib_n = left_tree.label + right_tree.label
        return Tree(fib_n,[left_tree,right_tree])

def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for branch in t.branches:
            all_leaves.extend(leaves(branch))
        return all_leaves

def prune(t, n):
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b,n)

print(fib_tree(6))
print(leaves(fib_tree(6)))
