import sys

num = int(sys.stdin.readline())

num = 2 ** num - num - 1

sys.stdout.write(str( num ))