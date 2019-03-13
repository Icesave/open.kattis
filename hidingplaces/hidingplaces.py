import sys
import operator
C = int( sys.stdin.readline().strip() )

def getLoc( s ):
    r = ord( s[0] ) - ord( "a" )
    c = int( s[1] ) - 1
    return r, c

def hashLoc( se ):
    x, y = se
    s = chr( x + ord( "a" ) )
    s += str( y + 1 )
    return s

def inRange( x, y ):
    if x > 7 or x < 0:
        return False
    if y > 7 or y < 0:
        return False
    return True

    
offs = [
    [-1, -2],
    [-1,  2],
    [ 1, -2],
    [ 1,  2],
    [-2, -1],
    [-2,  1],
    [ 2, -1],
    [ 2,  1],
]
for _ in range( C ):
    table = [[ -1 for _ in range( 8 ) ] for _ in range( 8 ) ]
    
    stack = [getLoc( sys.stdin.readline().strip() )]
    count = 0
    while True:
        tmp = []
        for pos in stack:
            x, y = pos 
            table[x][y] = count
            for off in offs:
                xt, yt = x+off[0], y+off[1]
                if  inRange( xt, yt ) and   \
                    table[xt][yt] == -1 and \
                    ( xt, yt ) not in tmp:
                    tmp.append( ( xt, yt ) )

        if tmp == []:
            break
        else:
            count += 1
            stack = tmp
    stack.sort( key = operator.itemgetter(0) )
    stack.sort( key = operator.itemgetter(1), reverse = True )
    r = str(count) + " " + " ".join(map( hashLoc, stack ))
    sys.stdout.write( r + '\n' )