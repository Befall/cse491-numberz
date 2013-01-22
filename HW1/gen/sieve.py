# Alex Lockwood - CSE 491 - HW #1

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def gen():
    _primeslist = [2]
    curr_num = 2

    while 1:
        if _is_prime(_primeslist, curr_num):
            _primeslist.append(curr_num)
            yield curr_num

        curr_num += 1
