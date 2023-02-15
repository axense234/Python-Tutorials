
file = open("random words", "r")
f = file.readlines()
print(f)
newlist = []
for line in f:
    if line[-1] == "\n":
        newlist.append(line[:-1])
    else:
        newlist.append(line)

print(newlist)

for line in f:
    if line[-1] == "\n":
        newlist.append(line.split())

print(newlist)
