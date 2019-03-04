import sys
matrix = []
tmp = []
for line in sys.stdin:
    if line == '\n':
        matrix.append( tmp )
        tmp = [] 
    else:
        for x in line.strip().split():
            tmp.append( int(x) )

if tmp != []:
    matrix.append( tmp )

i = 1
for case in matrix:
    sys.stdout.write( "Case " + str( i ) + ":" + '\n' )
    a, b, c, d = case
    det = 1/(a*d - b*c)
    sys.stdout.write( str(int( d*det )) + ' ' + str(int( -b*det )) + '\n' )
    sys.stdout.write( str(int( -c*det )) + ' ' + str(int( a*det )) + '\n' )
    i += 1