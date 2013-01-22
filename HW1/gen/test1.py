import sieve

for n, i in zip(range(5), sieve.gen()):
    print i
