import sys

class Node:
    def __init__( self, parent, size ):
        self.parent = parent
        self.size = size

def makeSet( x ):
    node = Node( None, 1 )
    nodes[x] = node

def find( node ):
    stack = []

    while node.parent != None:
        stack.append( node )
        node = node.parent

    for p in stack:
        p.parent = node
        
    return node

def union( node1, node2 ):
    node1 = find( node1 )
    node2 = find( node2 )
    
    if node1 == node2:
        return node1.size

    if node1.size < node2.size:
        node2.parent = node1
        node1.size += node2.size
        return node1.size        
    else:
        node1.parent = node2
        node2.size += node1.size
        return node2.size



N = int( sys.stdin.readline().strip() )
for _ in range( N ):
    nodes = {}

    F = int( sys.stdin.readline().strip() )
    for _ in range( F ):
        p1, p2 = sys.stdin.readline().strip().split( ' ' )
        
        if p1 not in nodes:
            makeSet( p1 )

        if p2 not in nodes:
            makeSet( p2 )

        res = union( nodes[p1], nodes[p2] )

        sys.stdout.write(str( res ) + '\n' )