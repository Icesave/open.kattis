import sys
from math import gcd

A, B = map( int, sys.stdin.readline().strip().split('/') )

A -= 32*B
A *= 5
B *= 9
d = gcd( A, B )
A = A // d 
B = B // d 

sys.stdout.write( str(A) + '/' + str(B) + '\n' )