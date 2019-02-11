import sys

for T in range( int(sys.stdin.readline().strip()) ):
    n = int(sys.stdin.readline().strip())
    v1 = sys.stdin.readline().strip().split( ' ' )
    v2 = sys.stdin.readline().strip().split( ' ' )
    for i in range( n ):
        v1[i] = int(v1[i])
        v2[i] = int(v2[i])

    v1.sort()
    v2.sort(reverse = True)
    r = 0
    for i in range( len(v1) ):
        r += int( v1[i] ) * int( v2[i] )
    sys.stdout.write( "Case #" + str(T+1) + ": " + str(r) + '\n' )