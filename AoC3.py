rucksack0 = []
with open('day3.txt') as f:
    rucksack = f.readlines()
    for line in rucksack:
        lines = line.strip('\n')
        rucksack0.append(lines)
items = []
priority = 0
for line in rucksack0:
    for i in range(len(line)//2):
        ok = False
        for j in range(len(line)//2, len(line)):
            if line[i] == line[j]:
                items.append(line[i])
                ok = True
                break
        if ok:
            break
for thing in items:
    if ord(thing) < 91:
        priority += ord(thing)-38
    else:
        priority += ord(thing)-96
print(priority)
