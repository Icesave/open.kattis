import sys

def po2(nr):
    r = 0
    pr = 0
    for i in range(nr): 
        pr = i//2
        po = 2**pr
        if po >= nr: 
            r = i+1
            break
        else:
            nr -= po
    return nr, r, pr

def middle(n, p, l):
    # Losa við prompt
    b = bin(n-1)[2:] 
    b = b.rjust(p, '0')

    l = len(b)-(l & 1)
        
    # Slicing er fljótast
    b = b[:l] + b[::-1] 

    return b 

N = int( sys.stdin.readline() )
if N < 2:
    sys.stdout.write( "1\n" )
elif N == 2:
    sys.stdout.write( "3\n" )
else:
    n, l, p = po2(N)

    # öll palindrome eru oddatölur
    # svo þær byrja og enda allar á 1
    b = '1' + middle(n, p, l) + '1'

    sys.stdout.write( str( int(b, 2) ) + '\n' )