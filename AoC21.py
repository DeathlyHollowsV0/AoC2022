with open('day2.txt') as file:
    games = []
    for line in file.readlines():
        line_elements = line.strip().split()
        games.append(line_elements)
score = 0
for i in range(len(games)):
    if games[i][0] == "A":
        if games[i][1] == "X":
            score += 3
        if games[i][1] == "Y":
            score += 4
        if games[i][1] == "Z":
            score += 8
    elif games[i][0] == "B":
        if games[i][1] == "X":
            score += 1
        elif games[i][1] == "Y":
            score += 5
        elif games[i][1] == "Z":
            score += 9
    elif games[i][0] == "C":
        if games[i][1] == "X":
            score += 2
        elif games[i][1] == "Y":
            score += 6
        elif games[i][1] == "Z":
            score += 7
print(score)
