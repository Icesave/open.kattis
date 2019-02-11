import sys
import re
while True:
    n = sys.stdin.readline().strip()
    if not n.isdigit():
        break
    n = int(n)
    freq = {}
    while True:
        line = sys.stdin.readline().strip()
        line = re.sub(r'\W+', ' ', line).split()
        if line == ["EndOfText"]:
            found = []
            for word, value in freq.items():
                if value == n:
                    found.append( word )
            if found == []:
                sys.stdout.write( "There is no such word.\n" )
            else:
                found.sort()
                for word in found:    
                    sys.stdout.write( word + '\n' )
            sys.stdout.write( '\n' )
            break 
        for word in line:
            if word.isalpha():
                word = word.lower()
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1

