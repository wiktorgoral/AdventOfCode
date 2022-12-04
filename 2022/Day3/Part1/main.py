file1 = open('data.txt', 'r')
rucksack = []
size: int = 0
line_current: str = ""

while True:
    line_current = file1.readline().rstrip()
    if not line_current:
        break

    rucksack.append(line_current)
    size += 1
file1.close()
LUT = {}

for i in range(26):
    LUT.update({chr(97 + i): i + 1})
    LUT.update({chr(65+i): i + 27})

summ = 0
for i in range(size):
    mid:int = int(len(rucksack[i])/2)
    comp_1 = rucksack[i][0:mid]
    comp_2 = rucksack[i][-mid:]
    res = ""
    for j in comp_1:
        if j in comp_2 and not j in res:
            res += j

    summ_temp = 0
    for j in range(len(res)):
        summ_temp += LUT[res[j]]
    summ += summ_temp
print(summ)
