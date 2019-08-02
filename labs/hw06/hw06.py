# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value
        self.prev_value = 0

    def next(self):
        if self.value == 0:
            return Fib(1)
        else:
            result = Fib(self.value+self.prev_value)
            result.prev_value = self.value
            return result

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self,item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price
        self.stock = 0
        self.balance = 0

    def deposit(self,sum_money):
        out_of_stock = self.stock == 0
        if out_of_stock:
            return 'Machine is out of stock. Here is your ${0}.'.format(sum_money)
        else:
            self.balance += sum_money
            return 'Current balance: ${0}'.format(self.balance)

    def vend(self):
        out_of_stock = self.stock == 0
        if out_of_stock:
            return 'Machine is out of stock.'
        else:
            if self.balance == self.item_price:
                self.stock -= 1
                return 'Here is your {0}.'.format(self.item_name)
            elif self.balance > self.item_price:
                self.stock -= 1
                change = self.balance - self.item_price
                self.balance = 0
                return 'Here is your {0} and ${1} change.'.format(self.item_name, change)
            elif self.balance < self.item_price:
                return 'You must deposit ${0} more.'.format(self.item_price-self.balance)

    def restock(self,quantity):
        self.stock += quantity
        return 'Current {0} stock: {1}'.format(self.item_name,self.stock)
