# https://www.hackerrank.com/challenges/waiter

from math import sqrt

def prime_iter(q):
    if q > 0:
        yield 2
        i = 3
    cnt = 1
    while cnt < q:
        if is_prime(i):
            cnt += 1
            yield i
        i += 2

def is_prime(n):
    max_int = int(sqrt(n)) + 1
    for i in xrange(3, max_int, 2):
        if n % i == 0:
            return False
    return True

def split_plates(lst, q):
    piles = []
    non_div_list = lst

    for p in prime_iter(q):
        div_list = []
        prev_list = non_div_list
        non_div_list = []

        while prev_list:
            plate = prev_list.pop()
            if plate % p:
                non_div_list.append(plate)
            else:
                div_list.append(plate)
        while div_list:
            print div_list.pop()
    while non_div_list:
            print non_div_list.pop()

def print_result(piles):
    for pile in piles:
        while pile:
            print pile.pop()

if __name__ == '__main__':
    n, q = map(int, raw_input().split())
    lst = map(int, raw_input().split())
    split_plates(lst, q)
