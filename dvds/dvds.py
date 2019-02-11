import sys

K = int( sys.stdin.readline() )

for _ in range( K ):
    N = int( sys.stdin.readline() )
    stack = map( int, sys.stdin.readline().split() )

    offset = 1
    for dvd in stack:
        if dvd == offset:
            offset = offset + 1
    offset = offset - 1

    sys.stdout.write( str( N - offset ) + '\n' )