file1 = open('data.txt', 'r')
matrix = []
size_y: int = 0
size_x: int = 0
line_current: str = ""

while True:
    line_current = file1.readline().rstrip()
    if size_y == 0:
        size_x = len(line_current)
    if not line_current:
        break

    matrix.append([])
    matrix[size_y] = ([x for x in line_current])
    size_y += 1
file1.close()

gamma: str = ""
epsilon: str = ""
for i in range(size_x):
    count_0: int = 0
    count_1: int = 0
    for j in range(size_y):
        if matrix[j][i] == "0":
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(gamma, int(gamma, 2), epsilon, int(epsilon, 2), int(gamma, 2) * int(epsilon, 2))
