import sys
import math
def bino( x, y ):
    a = math.factorial( x )
    b = math.factorial( y )
    c = math.factorial( x - y )
    div = a // (b * c)
    return div

N = int( sys.stdin.readline().strip() )

n = N + 1
res = bino( n*2, n ) // ( n + 1 )

sys.stdout.write(str( res ) + '\n' )
