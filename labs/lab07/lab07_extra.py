""" Optional Questions for Lab 07 """

from lab07 import *

# Q9
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty or link.rest is Link.empty:
        return
    else:
        next_link = link.rest
        while(not next_link is Link.empty and next_link.first == value):
            next_link = next_link.rest
        link.rest = next_link
        return remove_all(link.rest,value)


# Q10
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(Link(4)), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <<16>> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return
    else:
        ln_first = link.first
        if not isinstance(ln_first,Link):
            link.first = fn(link.first)
        else:
            while isinstance(ln_first.first,Link):
                ln_first = ln_first.first
            ln_first.first = fn(ln_first.first)
        deep_map_mut(fn,link.rest)


# Q11
def has_cycle(link):
    """Return whether link contains a cycle. Using "turtle and rabbit" strategy

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    link1 = link
    link2 = link.rest
    while(not link2 is Link.empty):
        if link1 is link2:
            break
        link1 = link1.rest
        if not link2.rest is Link.empty:
            link2 = link2.rest.rest
        else:
            link2 = link2.rest
    if  link2 is Link.empty:
        return False
    else:
        return True


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    # Same as above: Turtle and Rabbit


# Q12
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def reverse_helper(t, need_reversed):
        if t.is_leaf():
            return
        else:
            new_labels = [branch.label for branch in t.branches][::-1]
            for i in range(len(t.branches)):
                if need_reversed:
                    t.branches[i].label = new_labels[i]
                reverse_helper(t.branches[i], not need_reversed)
    return reverse_helper(t,True)
