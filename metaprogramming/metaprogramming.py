import sys
eiger = {}
for line in sys.stdin.readlines():
    line = line.strip().split( ' ' )
    if line[0] == "define" and len(line) == 3:
        defineable = True
        i = line[1]
        x = line[2]
        try:
            i = int(i)
            is_dig = True
        except ValueError:
            is_dig = False
        if is_dig and i >= -10000 and i <= 10000 and \
        x.isalpha() and x.islower() and len(x) <= 20:
            eiger[x] = i 
            continue
    elif line[0] == "eval" and len(line) == 4:
        x = line[1]
        y = line[2]
        z = line[3]

        if x in eiger and z in eiger:
            r = ''
            if  y == '<':
                if eiger[x] < eiger[z]:
                    r = True
                else:
                    r = False
            elif y == '>':
                if eiger[x] > eiger[z]:
                    r = True
                else:
                    r = False
            elif y == '=':
                if eiger[x] == eiger[z]:
                    r = True
                else:
                    r = False
                
            if r != '':
                if r:
                    sys.stdout.write( "true\n" )
                else:
                    sys.stdout.write( "false\n" )
                continue
    sys.stdout.write( "undefined\n" )
