rucksack0 = []
with open('day3.txt') as f:
    rucksack = f.readlines()
    for line in rucksack:
        lines = line.strip('\n')
        rucksack0.append(lines)
items = []
priority = 0
for l in range(0, len(rucksack0)-2, 3):
    for i in rucksack0[l]:
        ok = False
        for j in rucksack0[l+1]:
            for k in rucksack0[l+2]:
                if i == j == k:
                    items.append(i)
                    ok = True
                    break
            if ok:
                break
        if ok:
            break
for thing in items:
    if ord(thing) < 91:
        priority += ord(thing)-38
    else:
        priority += ord(thing)-96
print(priority)
