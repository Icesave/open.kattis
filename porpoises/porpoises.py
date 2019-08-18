import sys

P = int( sys.stdin.readline().strip() )

fibos = { 'a': 1, 'b': 2, 1: 1, 2: 1 }
mod = 1000000000
def fibo( n ):
    if n not in fibos:        
        if n % 2 == 0:
            a = n / 2
            x = fibo( a ) ** 2
            y = 2 * fibo( a ) * fibo( a - 1 )
            fibos[n] = ( x + y ) % mod
        else:
            a = ( n + 1 ) / 2
            x = fibo( a ) ** 2
            y = fibo( a - 1 ) ** 2
            fibos[n] = ( x + y ) % mod

    return fibos[n]

for _ in range( P ):
    K, Y = map( int, sys.stdin.readline().strip().split(" ") )
    y = fibo( Y )
    sys.stdout.write( str( K ) + " " + str( y ) + "\n" )