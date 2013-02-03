import sieve

for n, i in zip(range(5), sieve.gen()):
    if n == 5:
        assert i == 13
    print i
