import sys 
N = int( sys.stdin.readline().strip() )

for _ in range( N ):
    r = 0

    line = sys.stdin.readline().rstrip().split(',')
    l = len( line )
    for i in range( l ):
        if line[i] != '':
            num = int( line[i] )
            r += num * 60 ** (l-i-1)
    sys.stdout.write( str(r) + '\n' )
