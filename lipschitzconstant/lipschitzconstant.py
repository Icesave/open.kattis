import sys

def first( el ):
    return el[0]

N = int( sys.stdin.readline().strip() ) 
nums = []
for _ in range( N ):
    a = map( float, sys.stdin.readline().strip().split() )
    nums.append( list(a) )

nums.sort( key=first )

smallest = False
for i in range( 1, N ):
    x = nums[i][0] - nums[i-1][0]
    z = nums[i][1] - nums[i-1][1]
    f = abs( z/x )
    if not smallest:
        smallest = f
    elif smallest < f:
        smallest = f

sys.stdout.write( str(smallest) + '\n' )