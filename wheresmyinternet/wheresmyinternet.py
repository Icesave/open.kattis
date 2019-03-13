import sys
N, M = map( int, sys.stdin.readline().strip().split() )

def find( x ):
    while x != houses[x]:
        x = houses[x]
    return x

def merge( a, b ):
    a = find( a )
    b = find( b )
    if a < b:
        houses[a] = b
    else:
        houses[b] = a


houses = {x : x for x in range( N )}
for _ in range( M ):
    a, b = map( int, sys.stdin.readline().strip().split() )
    merge( a-1, b-1 )



connected = True
root = find(0)
for x in range( N ):
    if find(x) != root:
        connected = False
        sys.stdout.write(str( x+1 ) + '\n' )

if connected:
    sys.stdout.write( "Connected\n" )
