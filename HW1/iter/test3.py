import sieve
count = 0

for i in sieve.prime_tester():
    print i
    count += 1
    
    if count >= 20:
        break
