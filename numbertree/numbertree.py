import sys
ins = sys.stdin.readline().strip().split()
H = int( ins[0] )
res = 1
if len(ins) == 2:
    for s in ins[1]:
        res = res * 2
        if( s == 'R' ):
            res = res + 1
res = 2**( H+1 ) - res

sys.stdout.write(str( res ) + '\n' )