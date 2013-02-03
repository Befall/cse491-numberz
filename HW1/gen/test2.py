import sieve

for n, i in zip(range(10), sieve.gen()):
    if n == 8:
        assert i == 23
    print i
