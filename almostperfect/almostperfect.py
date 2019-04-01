import sys
from math import log
def findPrimes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes = findPrimes(1000000)
divisors = { 1:1 }
for p in primes:
    divisors[p] = p+1


def powerOf(n,p):
    c = 0
    while n%p == 0:
        c += 1
        n /= p
    return c, n

def divisor(n):
    if n in divisors:
        return divisors[n]
    
    i = 0
    while n%primes[i] != 0:
        i += 1
    p = primes[i]
    c, r = powerOf(n,p)
    s = (p**(c+1)-1)/(p-1)
    divisors[n] = divisor(r)*s
    return divisors[n]

for line in sys.stdin:
    if line == '':
        break
    num = int(line.strip())

    d = divisor(num)
    d -= num*2

    sys.stdout.write( str( num ) )
    if d == 0:
        sys.stdout.write( " perfect" + '\n' )
    elif d >= -2 and d <= 2:
        sys.stdout.write( " almost perfect" + '\n' )
    else:
        sys.stdout.write( " not perfect" + '\n' )