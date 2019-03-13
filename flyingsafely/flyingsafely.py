import sys
C = int( sys.stdin.readline().strip() )

for _ in range( C ):
    # N = number of cities
    # M = number of pilots
    N, M = map( int, sys.stdin.readline().strip().split(" ") )
    
    sys.stdout.write(str( N-1 ) + '\n' )

    for _ in range( M ):
        trash = sys.stdin.readline().strip().split(" ")
