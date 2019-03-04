import sys

class Node:
    def __init__( self, parent, size ):
        self.parent = parent
        self.size = size

def makeSet( x ):
    node = Node( None, len(x) )
    thesaurus[x] = node

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
        return node1.size        
    else:
        node1.parent = node2
        return node2.size


N, M = map(int, sys.stdin.readline().strip().split() )

essay = []
thesaurus = {}

for word in sys.stdin.readline().strip().split():
    makeSet( word )
    essay.append( word )

for _ in range( M ):
    a, b = sys.stdin.readline().strip().split()
    
    if a not in thesaurus:
        makeSet( a )

    if b not in thesaurus:
        makeSet( b )

    union( thesaurus[a], thesaurus[b] )

res = 0
for word in essay:
    word = find( thesaurus[word] )
    res += word.size

sys.stdout.write(str( res ) + '\n' )