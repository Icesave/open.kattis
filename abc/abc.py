import sys

lines = sys.stdin.read().splitlines()

nums = sorted([ int(x) for x in lines[0].split(' ') ])

s = []
for x in lines[1]:
    if x == 'A':
        s.append(str( nums[0]) )
    elif x == 'B':
        s.append(str( nums[1]) )
    elif x == 'C':
        s.append(str( nums[2]) )
        
sys.stdout.write( ' '.join(s) )