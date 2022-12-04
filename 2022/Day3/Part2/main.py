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
for i in range(int(size/3)):
    set_1 = set(rucksack[i*3])
    set_2 = set(rucksack[i * 3 + 1])
    set_3 = set(rucksack[i * 3 + 2])

    res = list(set.intersection(set_1, set_2, set_3))

    summ_temp = 0
    for j in range(len(res)):
        summ_temp += LUT[res[j]]
    summ += summ_temp
print(summ)
