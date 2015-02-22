workfile = "mlfixedreduced"
f = open(workfile+".txt", 'r')
stuff = ""
for line in f:
    x = 0
    if "Business sector" in line:
        x = 1
    if "business" in line:
        x = 1
    if "x 1000)" in line:
        x = 1
    elif "employe" in line:
        x = 1
    elif "Labour income" in line:
        x = 1
    if x == 0:
        stuff = stuff + line
print "done"
f.close()
f = open(workfile+".txt", 'w')
f.write(stuff)
f.close()
