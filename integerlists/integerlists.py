import sys

def execute( p, a, n ):  
    r = 0
    s = n
    reverse = False

    for cmd in p:
        if( cmd == 'R' ):
            reverse = not(reverse)
        if( cmd == 'D' ):
            if n == 0:
                return -1
            elif reverse:
                s -= 1
            else:
                r += 1
            n -= 1
    if reverse:
        return list(reversed( a[r:s] ))
    return a[r:s]



N = int( sys.stdin.readline().strip() )

for _ in range( N ):
    p = sys.stdin.readline().strip()
    n = int( sys.stdin.readline().strip() )
    a = sys.stdin.readline().strip()[1:-1].split( ',' )

    res = execute( p, a, n )
    if res == -1:
        sys.stdout.write( "error\n" )
    else:
        sys.stdout.write( "[" )
        sys.stdout.write( ','.join(res) )
        sys.stdout.write( "]\n" )


