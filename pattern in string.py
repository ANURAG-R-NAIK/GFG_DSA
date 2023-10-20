str = input('enter the string')
pat = input('enter the pattern')
pos = str.find(pat)

while pos >= 0:
    print(pos)
    pos = str.find(pat, pos+1)