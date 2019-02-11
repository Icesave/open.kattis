import sys
n = int(sys.stdin.readline().strip())
cost = []
for num in sys.stdin.readline().strip().split():
    cost.append(int( num ))

cost.sort(reverse = True)

r = 0
if n > 2:
    for i in range( 2, n, 3 ):
        r += cost[i]

sys.stdout.write( str(r)+'\n' )