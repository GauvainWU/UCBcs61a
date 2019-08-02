"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    # def func2(x):
    #     def func3(y):
    #         return func(x,y)
    #     return func3
    return lambda arg1 : lambda arg2: func(arg1,arg2)
