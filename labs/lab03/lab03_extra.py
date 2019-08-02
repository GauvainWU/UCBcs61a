""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def is_prime_helper(i):
        if i == 1:
            return True
        else:
            if (n % i) == 0:
                return False
            else:
                return is_prime_helper(i-1)
    return is_prime_helper(n-1)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if(a<b):
        a,b = b,a
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)

def num_appearance(number,digit):
    count = 0
    for i in range(len(str(number))):
        count += int(str(number)[i]) == digit
    return count

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def helper(i):
        if(i==5):
            num_app = num_appearance(n,5)
            return num_app * (num_app - 1) // 2
        else:
            return num_appearance(n,i)*num_appearance(n,10-i) + helper(i+1)
    return helper(1)
