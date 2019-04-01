import sys
T = int( sys.stdin.readline().strip() )

mod = 1000000007
fib = [1, 2]

for _ in range( T ):
    N = int( sys.stdin.readline().strip() )
    if len(fib) <= N:
        n = len(fib)
        while n <= N:
            nex = fib[n-1] + fib[n-2]
            fib.append(nex % mod)
            n += 1

    sys.stdout.write(str( fib[N] ) + '\n' )

