import sys

words = sys.stdin.readline().strip().split(' ')

r = 'yes'
used = []

for word in words:
    if word in used:
        r = 'no'
        break
    else:
        used.append( word )    
        
sys.stdout.write(str( r ))