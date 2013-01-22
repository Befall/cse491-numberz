import sieve

for n, i in zip(range(15), sieve.gen()):
    print i
