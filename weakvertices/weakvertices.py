import sys

def findTriangles( g, v ):
    for i in range(len( v )):
        if v[i] == 1:
            for x in range( i, len( v )):
                if v[x] == 1 and g[i][x] == 1:
                    return True
    return False

while True:
    N = int( sys.stdin.readline().strip() )

    if N == -1:
        break
    
    strong = { x : False for x in range( N ) }
    graph = [ 
        list(map( int, sys.stdin.readline().strip().split() )) 
        for _ in range( N ) 
    ]
    for i in range( N ):
        if not strong[i]:
            strong[i] = findTriangles( graph, graph[i] )
 
    for i in range( N ):
        if not strong[i]:
            sys.stdout.write(str( i ) + " " )
    
    sys.stdout.write( "\n" )
    
    
