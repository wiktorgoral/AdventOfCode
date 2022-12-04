file1 = open('data.txt', 'r')
player_1 = []
player_2 = []
size: int = 0
line_current: str = ""

while True:
    line_current = file1.readline().rstrip()
    if not line_current:
        break

    mid = line_current.index(",")
    player_1.append(line_current[0:mid])
    player_2.append(line_current[mid + 1:])
    size += 1
file1.close()

summ = 0
for i in range(size):
    mid = player_1[i].index("-")
    elf1 = [x for x in range(int(player_1[i][0:mid]), int(player_1[i][mid + 1:]) + 1)]
    mid = player_2[i].index("-")
    elf2 = [x for x in range(int(player_2[i][0:mid]), int(player_2[i][mid + 1:]) + 1)]

    if set.intersection(set(elf1), set(elf2)) == set(elf1) or set.intersection(set(elf1), set(elf2)) == set(elf2):
        summ += 1
        print(i)

print(summ)
