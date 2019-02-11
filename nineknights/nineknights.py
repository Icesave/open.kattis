import sys

board = []

found = 0
for _ in range( 5 ):
    tmp = []
    for c in sys.stdin.readline():
        if( c == 'k' ):
            found += 1
            tmp.append( True )
        elif( c == '.' ) :
            tmp.append( False )
    board.append( tmp )

if found != 9:
    sys.stdout.write( "invalid" )
    sys.exit(0)



def colliding( x, y ):
    if x < 0 or y < 0 \
    or x >= 5 or y >= 5: 
        return False
    elif board[x][y]: 
        return True
    else:
        return False

for x in range( 5 ):
    for y in range( 5 ):
        if board[x][y]:
            if colliding( x-2, y-1 ) \
            or colliding( x-1, y-2 ) \
            or colliding( x+1, y-2 ) \
            or colliding( x+2, y-1 ) \
            or colliding( x-2, y+1 ) \
            or colliding( x-1, y+2 ) \
            or colliding( x+1, y+2 ) \
            or colliding( x+2, y+1 ) :
                sys.stdout.write( "invalid" )
                sys.exit(0)

sys.stdout.write( "valid" )