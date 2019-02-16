import sys

class Stack:
    def __init__( self ):
        self.items = []
        self.nex = 0

    def isEmpty( self ):
        return self.items == []

    def push( self, x ):
        if len( self.items ) == self.nex:
            self.items.append( x )
        else:
            self.items[self.nex] = x
        self.nex += 1
    
    def pop( self ):
        if self.nex > 0:
            self.nex -= 1 
    
    def toString( self ):
        for x in range( self.nex ):
            sys.stdout.write( self.items[x] )

line = sys.stdin.readline().strip()
s = Stack()
for c in line:
    if c == '<':
        s.pop()
    else:
        s.push( c )
s.toString() 