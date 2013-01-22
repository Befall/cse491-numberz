# Alex Lockwood - CSE 491 - HW #1

class prime_tester(object):
    def __init__(self):
        self._primeslist = [2]

    def __iter__(self):
        return self
    
    def is_prime(self, n):
        for i in self._primeslist:
            if n % i == 0:
                return False
        return True

    def next(self):
        start = self._primeslist[-1] + 1
        while 1:
            if self.is_prime(start):
                self._primeslist.append(start)
                return start

            start += 1
