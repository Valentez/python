instr = input("Please input a few words: ")
instr = instr.split()
for i, j in enumerate(instr, 1):
    print(i, j[:10])
