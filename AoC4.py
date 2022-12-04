pair = []
numpairs = 0
with open('day4.txt') as f:
    lines = f.readlines()
    for line in lines:
        pair.append(line.strip("\n").replace(
            "-", " ").replace(",", " ").split())
for line in pair:
    if int(line[0]) <= int(line[2]) and int(line[1]) >= int(line[3]) or int(line[0]) >= int(line[2]) and int(line[1]) <= int(line[3]):
        numpairs = numpairs + 1
print(numpairs)
                                                                                                              
