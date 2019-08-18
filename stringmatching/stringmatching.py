import sys
  
def computeLPSArray( pat, M, lps ): 
    l = 0 
    lps[0] 
    i = 1
    while i < M: 
        if pat[i] == pat[l]: 
            l += 1
            lps[i] = l
            i += 1
        else: 
            if l != 0: 
                l = lps[l-1] 
            else: 
                lps[i] = 0
                i += 1

def KMPSearch( pat, txt ): 
    found = []

    M = len( pat ) 
    N = len( txt ) 
    
    lps = [0] * M 
    j = 0 
    computeLPSArray( pat, M, lps ) 
  
    i = 0
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            found.append( str( i - j ) )
            j = lps[j-1] 
        elif i < N and pat[j] != txt[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    return found

while True:
    pattern = sys.stdin.readline().strip()
    if pattern == '':
        break
    text = sys.stdin.readline().strip()
    indexes = KMPSearch( pattern, text )
    sys.stdout.write( ' '.join( indexes ) + '\n' )
    