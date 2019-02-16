import sys

class Queue:
    def __init__( self ):
        self.list = []

    def enqueue( self, x ):
        self.list.append( x )

    def denqueue( self ):
        if self.isEmpty():
            return None
        else:
            return self.list.pop( 0 )

    def isEmpty( self ):
        return self.list == []

def distance( x1, y1, x2, y2 ):
    x = abs( x1 - x2 )
    y = abs( y1 - y2 )
    return x + y

t = int( sys.stdin.readline().strip() )

for _ in range( t ):
    n = int( sys.stdin.readline().strip() )


    points = []
    for _ in range( n + 2 ):
        x, y = map( int, sys.stdin.readline().strip().split())
        points.append( [x, y] )

    visted = [False]*(n+2)
    q = Queue()
    q.enqueue( 0 )
    while not q.isEmpty():
        x = q.denqueue()
        if not visted[x]:
            visted[x] = True
            x1, y1 = points[x]
            for i in range( n+2 ):
                x2, y2 = points[i]
                if distance( x1, y1, x2, y2 ) <= 1000:    
                    q.enqueue( i )
    if visted[n+1]:
        sys.stdout.write( "happy\n" )
    else:
        sys.stdout.write( "sad\n" )
