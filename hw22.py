inlist = input("Input elements for list with space: ")
inlist = inlist.split()
for i in range(0, len(inlist)-1, 2):
    inlist[i], inlist[i+1] = inlist[i+1], inlist[i]
print(inlist)
