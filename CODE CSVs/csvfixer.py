workfile = "masterlist"
f = open(workfile+".txt", 'r')
stuff = f.read()
f.close()
quote = 0
newstuff = ""
for letter in stuff:
    if letter == '"' and quote == 0:
        quote = 1
    elif letter == '"':
        quote = 0
    elif not(letter == ',' and quote == 1):
        newstuff = newstuff + letter
f = open(workfile+"fixed.txt", 'w')
f.write(newstuff)
f.close()
