j = 0

with open('day1.txt', 'r') as file:
    file2 = file.readlines()
tab = [0]*len(file2)

for i in range(len(file2)):
    try:
        tab[j] += int(file2[i])
    except ValueError:
        j += 1
rabsort = sorted(tab, reverse=True)
print(rabsort[0] + rabsort[1] + rabsort[2])
