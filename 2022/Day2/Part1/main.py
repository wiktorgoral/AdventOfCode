file1 = open('data.txt', 'r')
player_1 = []
player_2 = []
size: int = 0
line_current: str = ""

while True:
    line_current = file1.readline().rstrip()
    if not line_current:
        break


    player_1.append(line_current[0])
    player_2.append(line_current[2])
    size += 1
file1.close()


summ: int = 0
for i in range(size):
    if player_2[i] == "X":
        summ += 1
    elif player_2[i] == "Y":
        summ += 2
    else:
        summ += 3

    if player_2[i] == "X" and player_1[i] == "A" or player_2[i] == "Y" and player_1[i] == "B" or player_2[i] == "Z" and \
            player_1[i] == "C":
        summ += 3
    else:
        if player_2[i] == "X" and player_1[i] == "C":
            summ += 6
        elif player_2[i] == "Y" and player_1[i] == "A":
            summ += 6
        elif player_2[i] == "Z" and player_1[i] == "B":
            summ += 6
        else:
            summ += 0

print(summ)
