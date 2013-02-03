import sieve

def test1():
    count = 0
    for i in sieve.prime_tester():
        print i
        count += 1
        
        if count >= 10:
            assert i == 31
            break

def test2():
    p = sieve.prime_tester()
    i = iter(p)
    assert i.next() == 2

test1()
test2()
