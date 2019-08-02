from lab07 import *
def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5, 6, 7])
    7
    >>> m([1, 2, 3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """
    temp_max = -float("inf")
    def max_finder(lst):
        nonlocal temp_max
        temp_max = max(max(lst),temp_max)
        return max(max(lst),temp_max)
    return max_finder

def filter_tree(t,fn):
    """
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(6,[Tree(7)])])
    >>> filter_tree(t, lambda x: x % 2 != 0)
    >>> t
    tree(1, [Tree(3)])
    >>> t2 = Tree(2, [Tree(3), Tree(4), Tree(5)])
    >>> filter_tree(t2, lambda x: x != 2)
    >>> t2
    Tree(2)
    """
    if not fn(t.label):
        t.branches = []
    else:
        for branch in t.branches:
            if not fn(branch.label):
                t.branches.remove(branch)
            else:
                return filter_tree(branch,fn)

def nth_level_tree_map(fn, tree, n):
    """Mutates a tree by mapping a function all the elements of a tree.
    >>> tree = Tree(1, [Tree(7, [Tree(3), Tree(4), Tree(5)]), Tree(2, [Tree(6), Tree(4)])])
    >>> nth_level_tree_map(lambda x: x + 1, tree, 2)
    >>> tree
    Tree(2, [Tree(7, [Tree(4), Tree(5), Tree(6)]), Tree(2, [Tree(7), Tree(5)])])
    """
    tree.label = fn(tree.label)
    level = 1
    next_level = tree.branches
    while next_level:
        if level % n == 0:
            for branch in next_level:
                branch.label = fn(branch.label)
        level = level + 1
        next_level = sum([branch.branches for branch in next_level],[])

def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    if sub_link is Link.empty:
        return True
    if link is Link.empty:
        return False
    if link.first == sub_link.first:
        return seq_in_link(link.rest,sub_link.rest)
    else:
        return seq_in_link(link.rest,sub_link)

def gen_inf(lst):
    """
    >>> t = gen_inf([3, 4, 5])
    >>> next(t)
    3
    >>> next(t)
    4
    >>> next(t)
    5
    >>> next(t)
    3
    >>> next(t)
    4
    """
    while True:
        for element in lst:
            yield element

def nested_gen(lst):
    '''
    >>> a = [1, 2, 3]
    >>> def g(lst):
    >>>     for i in lst:
    >>>         yield i
    >>> b = g([10, 11, 12])
    >>> c = g([b])
    >>> lst = [a, c, [[[2]]]]
    >>> list(nested_gen(lst))
    [1, 2, 3, 10, 11, 12, 2]
    '''
    
