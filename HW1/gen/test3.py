import sieve

for n, i in zip(range(15), sieve.gen()):
    if n == 13:
        assert i == 47
    print i
