import sieve

for n, i in zip(range(10), sieve.gen()):
    print i
