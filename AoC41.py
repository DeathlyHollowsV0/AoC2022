pair = []
overlap = 0
with open('day4.txt') as f:
    lines = f.readlines()
    for line in lines:
        pair.append(line.strip("\n").replace(
            "-", " ").replace(",", " ").split())
for line in pair:
    if (int(line[2]) <= int(line[1]) and (int(line[2]) >= int(line[0]))) or (int(line[0]) <= int(line[3]) and int(line[0]) >= int(line[2])):
        overlap = overlap + 1
print(overlap)
