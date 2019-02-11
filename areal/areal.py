import sys
from decimal import getcontext, Decimal

num = int( sys.stdin.readline() )

getcontext().prec = 1024
num = Decimal(num).sqrt()
num = num * 4

sys.stdout.write(str( num ))