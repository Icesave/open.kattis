import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
    d = int(sys.stdin.readline().strip())
    mod = 1000000007
    res = 8 * pow(9, d-1, mod) % mod
    sys.stdout.write(str(res) + "\n")
