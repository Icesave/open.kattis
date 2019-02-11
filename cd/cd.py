#Python 2.7
import sys

while True:
    ins = sys.stdin.readline().split()
    N = int( ins[0] )
    M = int( ins[1] )

    if N == 0 and M == 0:
        break

    a = set() 
    for _ in xrange( N ): 
        a.add(int( sys.stdin.readline() ))
    
    ans = 0
    for _ in xrange( M ):
        if int( sys.stdin.readline() ) in a:
            ans += 1

    sys.stdout.write(str( ans ) + '\n')
