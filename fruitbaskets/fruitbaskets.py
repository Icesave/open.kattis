import sys
n = int(sys.stdin.readline().strip())


fruits = []
cost = 0
for fruit in sys.stdin.readline().strip().split():
    fruits.append(int( fruit ))
    cost += int( fruit )

cost *= 2**(n-1)

def subsetsUnder200( i, r ):
    global cost 
    r += fruits[i]
    if r < 200:
        cost -= r
        for x in range( i+1, n ):
            subsetsUnder200( x, r )
            


for i in range( n ):
    subsetsUnder200( i, 0 )

sys.stdout.write(str( cost ) + '\n' )