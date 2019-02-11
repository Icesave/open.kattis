import sys

h = 1001
l = 0
ans = ""

while ans != "correct":
    guess = round( (h + l)/2 )
    sys.stdout.write(str( guess ) + "\n")
    sys.stdout.flush()
    ans = sys.stdin.readline().strip()

    if ans == "lower":
        h = guess
    elif ans == "higher":
        l = guess
