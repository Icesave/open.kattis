import sys

while True:
    N = int( sys.stdin.readline().strip() )
    if N == 0:
        break
    names = [ sys.stdin.readline().strip() for _ in range( N ) ]
    names = sorted( names, key = lambda x : x[:2] )
    for name in names:
        sys.stdout.write( str( name ) + '\n' )
    sys.stdout.write( '\n' )