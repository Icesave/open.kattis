import sys
N = int( sys.stdin.readline().strip() )

longest = [1]
n = 1
while n <= N/2:
    n *= 2
    longest.append(n)

size = len( longest )

sys.stdout.write(str( size ) + '\n' )
sys.stdout.write( " ".join(map( str, longest )) + '\n' )
