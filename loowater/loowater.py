import sys
while True:
    n, m = map( int, sys.stdin.readline().strip().split() )
    if n == 0 and m == 0:
        break
    if n > m:
        sys.stdout.write( "Loowater is doomed!\n" )
        for _ in range( n ):
            sys.stdin.readline()
        for _ in range( m ):
            sys.stdin.readline()
        continue

    dragon = []
    knights = []
    for _ in range( n ):
        dragon.append(int( sys.stdin.readline().strip() ))
    dragon.sort()
    
    for _ in range( m ):
        knights.append(int( sys.stdin.readline().strip() ))
    knights.sort()
    
    coins = 0
    d = 0
    for k in range(len( knights )):
        if d == n:
            break
        if knights[k] >= dragon[d]:
            d += 1
            coins += knights[k]

    if( d == n ):
        sys.stdout.write( str(coins) + '\n' )    
    else:
        sys.stdout.write( "Loowater is doomed!\n" )