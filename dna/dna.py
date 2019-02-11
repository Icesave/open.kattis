import sys

N = int( sys.stdin.readline().strip() ) 
a = list( sys.stdin.readline().strip() )[::-1]
r = 0
mul = True
for x in range( N-1 ):
    if mul:
        if a[x] == 'A':
            continue
        if a[x+1] != 'A':
            mul = False
    else:
        if a[x] == 'B':
            continue
        if a[x+1] != 'B':
            mul = True

    r += 1

if not( mul and a[N-1] == 'A' or not mul and a[N-1] == 'B' ):
    r += 1
sys.stdout.write(str( r ) + '\n' )
