""" Homework 2: Higher Order Functions"""

HW_SOURCE_FILE = 'hw02.py'

from math import log
from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

######################
# Required Questions #
######################
def product(n, term):
    """Return the product of the first n terms in a sequence.
    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product', ['Recursion'])
    True
    """
    result = 1
    i = 1
    while(i<=n):
        result *= term(i)
        i = i + 1
    return result


def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)  # 4 * 3 * 2 * 1
    24
    >>> factorial(6)  # 6 * 5 * 4 * 3 * 2 * 1
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    return product(n,lambda x:x)

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    i = 2
    result = 1
    result = combiner(base,term(1))
    if(n==0):
        return base
    while(i<=n):
        result = combiner(result,term(i))
        i = i + 1
    return result

def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(add,0,n,term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(mul,1,n,term)

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def make_repeater(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    def repeated(x):
        for i in range(n):
            x = f(x)
        return x
    return repeated

def num_sevens(n):
    """Returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if(n==0):
        return 0
    else:
        if n % 10 == 7:
            return num_sevens(n//10) + 1
        else:
            return num_sevens(n//10)

def direction(n):
    """
    Return true if the number should increment in increasing order and return
    false if not

    >>> direction(3)
    True
    >>> direction(8)
    False
    >>> direction(15)
    True
    """
    if(n==1):
        return True
    else:
        if (num_sevens(n)>0 or n % 7 == 0):
            return not direction(n-1)
        else:
            return direction(n-1)



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    if(n==1):
        return 1
    else:
        if(direction(n-1)):
            return pingpong(n-1)+1
        else:
            return pingpong(n-1)-1

def pingpong_assign(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong_assign(7)
    7
    >>> pingpong_assign(8)
    6
    >>> pingpong_assign(15)
    1
    >>> pingpong_assign(21)
    -1
    >>> pingpong_assign(22)
    0
    >>> pingpong_assign(30)
    6
    >>> pingpong_assign(68)
    2
    >>> pingpong_assign(69)
    1
    >>> pingpong_assign(70)
    0
    >>> pingpong_assign(71)
    1
    >>> pingpong_assign(72)
    0
    >>> pingpong_assign(100)
    2
    """
    result = 0
    counter = 0
    direction = True
    while(counter<n):
        if direction:
            result = result + 1
        else:
            result = result - 1
        counter = counter + 1
        if num_sevens(counter)>0 or counter % 7 == 0:
            direction = not direction
    return result


def count_partition_pow_2(n,m):
    """
    Inspired from the count_partition(n,m) that is used to calculate the number
    of partition of a number n using numbers up to m(no greater than m).
    e.g. count_partition(6,3):
    6 = 3 + 3
    6 = 3 + 2 + 1
    6 = 3 + 1 + 1 + 1 (count_partition(6-3,3))
    6 = 2 + 2 + 2
    6 = 2 + 2 + 1 + 1
    6 = 2 + 1 + 1 + 1 + 1(count_partition(6,2))
    6 = 1 + 1 + 1 + 1 + 1 + 1 (count_partition(6,1))
    count_partition(n,m) = count_partition(n-m,m) + count_partition(n,m-1)
    m must be a power of 2
    """
    if (n == 1 or m == 1):
        return 1
    elif(n <= 0 or m <= 0):
        return 0
    elif(n == m and abs(pow(2,int(log(n,2)))-n)<1e-10):
        return count_partition_pow_2(n,m//2) + count_partition_pow_2(n-m,m) + 1
    else:
        return count_partition_pow_2(n,m//2) + count_partition_pow_2(n-m,m)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    return count_partition_pow_2(amount,pow(2,int(log(amount,2))))




###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'

def merge_while(s1, s2):
    """ Merges two sorted lists
    >>> merge_while([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge_while([1, 2], [])
    [1, 2]
    """
    result = []
    i = 0
    j = 0
    if(len(s1)==0):
        return s2
    elif(len(s2)==0):
        return s1
    else:
        while(i<len(s1) or j<len(s2)):
            if ((i==len(s1) and j<=len(s2)) or s1[i]>s2[j]):
                result.append(s2[j])
                j = j + 1
            elif((j==len(s2) and i<=len(s1)) or s1[i]<=s2[j]):
                result.append(s1[i])
                i = i + 1
        return result

def merge(s1,s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if(len(s1)==0):
        return s2
    elif(len(s2)==0):
        return s1
    else:
        if(s1[0]<s2[0]):
            return [s1.pop(0)] + merge(s1,s2)
        else:
            return [s2.pop(0)] + merge(s1,s2)

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.
    >>> mario_number(' P P ') # jump, jump
    1
    >>> mario_number(' P P  ') # jump, jump, step
    1
    >>> mario_number('  P P ') # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ') # Mario cannot jump two plants
    0
    >>> mario_number('    ')
    3
    >>> mario_number('    P    ')
    9
    >>> 
    """
    if('PP' in level):
        return 0
    elif(level == ' ' or level == '  '):
        return 1
    else:
        if(level[0:3] == '   '):
            return mario_number(level[2:])+mario_number(level[1:])
        elif(level[0:3]== '  P'):
            return mario_number(level[1:])
        elif(level[0:2] == ' P'):
            return mario_number(level[2:])
