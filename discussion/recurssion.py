def split(n):
    all_but_last, last = n//10, n % 10
    return all_but_last, last

def sum_every_other_digit(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_every_other_digit_double(all_but_last) + last

def sum_every_other_digit_double(n):
    if n < 10:
        return 0
    else:
        all_but_last, last = split(n)
        return sum_every_other_digit(all_but_last)
