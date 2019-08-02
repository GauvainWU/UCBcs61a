from lab07 import *

def multiply_link(lst_of_link):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_link([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    end = False
    new_lst_of_link = lst_of_link
    product_first = []
    result_link = Link.empty
    while not end:
        result_first = 1
        for link in new_lst_of_link:
            end = end or (link.rest is Link.empty)
            result_first *= link.first
        product_first.append(result_first)
        new_lst_of_link = [link.rest for link in new_lst_of_link]
    for product in product_first[::-1]:
        result_link = Link(product,result_link)
    return result_link

def remove_duplicates(link):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    if link is Link.empty or link.rest is Link.empty:
        return
    else:
        while link.second == link.first:
            link.rest = link.rest.rest
        return remove_duplicates(link.rest)

def even_weighted(lst):
    """
    >>> x = [1,2,3,4,5,6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [ind*element for ind,element in enumerate(lst) if ind % 2 == 0]

def quicksort_list(lst):
    """
    >>> quicksort_list([3,1,4,5,2,0,10])
    [0, 1, 2, 3, 4, 5, 10]
    """
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    less = [element for element in lst if element < pivot]
    greater = [element for element in lst if element > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

def max_product(lst):
    """
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(lst) == 0:
        return 1
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return max(lst)
    else:
        return max(lst[0]*max_product(lst[2:]), max_product(lst[1:]))

def print_levels(tree):
    print([tree.label])
    next_level = tree.branches
    while next_level:
        curr_list = [branch.label for branch in next_level]
        print(curr_list)
        next_level = sum([branch.branches for branch in next_level],[])

def redundant_map(t,f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> redundant_map(tree, double)
    >>> print_levels(tree)
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    depth = 0
    t.label = f(t.label)
    next_level = t.branches
    while next_level:
        depth += 1
        for branch in next_level:
            for _ in range(2**time):
                branch.label = f(branch.label)
        next_level = sum([branch.branches for branch in next_level],[])

# Official Solution
def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> redundant_map(tree, double)
    >>> print_levels(tree)
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label =f(t.label)
    new_f = lambda x: f(f(x))
    for b in t.branches:
        redundant_map(b, new_f)
