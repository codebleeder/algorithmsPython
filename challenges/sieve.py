__author__ = 'cloudera'


def sieve(A):
        if A == 1:
            return [1]
        primes = range(2,A+1)
        primes2 = []
        for i in primes:
            if i != 1:
                for j in xrangeprimes[i+1:]:
                    if i%j==0:
                        j = 1
        for i in primes:
            if i != 1:
                primes2.append(i)
        return primes2

print sieve(10)
