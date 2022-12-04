file1 = open('data.txt', 'r')
player_1 = []
player_2 = []
outcome=[]
size: int = 0
line_current: str = ""

while True:
    line_current = file1.readline().rstrip()
    if not line_current:
        break


    player_1.append(line_current[0])
    outcome.append(line_current[2])
    size += 1
file1.close()


for i in range(size):
    if outcome[i]=="Y":player_2.append(player_1[i])
    elif outcome[i]=="X":
        if player_1[i] == "A": player_2.append("C")
        elif player_1[i] == "B": player_2.append("A")
        else: player_2.append("B")
    else:
        if player_1[i] == "C": player_2.append("A")
        elif player_1[i] == "A": player_2.append("B")
        else: player_2.append("C")

summ=0
for i in range(size):
    if outcome[i]=="X": summ+=0
    elif outcome[i]=="Y": summ+=3
    else: summ+=6

    if player_2[i]=="A": summ+=1
    elif player_2[i]=="B": summ+=2
    else: summ +=3



print(summ)
