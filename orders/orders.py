import sys

N = int( sys.stdin.readline().strip() ) 
items = []
maxItem = 0
for item in sys.stdin.readline().strip().split():
    item = int( item )
    if item > maxItem:
        maxItem = item
    items.append( item )


M = int( sys.stdin.readline().strip() ) 
orders = []
maxOrder = 0
for order in sys.stdin.readline().strip().split():
    order = int( order )
    if order > maxOrder:
        maxOrder = order
    orders.append( order )

maxValue = maxOrder+maxItem
a = [-2]*(maxValue)
a[0] = 0
for x in range( N ):
    item = items[x]
    i = 0
    while i+item < maxValue:
        if a[i] >= 0:
            if a[i+item] == -2:
                a[i+item] = x
            else:
                a[i+item] = -1
        if a[i] == -1:
            a[i+item] = -1
        i += 1


for order in orders:
    if(a[order] == -2):
        sys.stdout.write( "Impossible" )
    elif(a[order] == -1):
        sys.stdout.write( "Ambiguous" )
    else:
        r = []
        while( order > 0 ):
            r.append( a[order]+1 )
            order -= items[ a[order] ]

        if( order < 0 ):
            sys.stdout.write( "Ambiguous" )
        else:
            r.sort()
            for num in r:
                sys.stdout.write(str( num ) + " " )
    sys.stdout.write( '\n' )