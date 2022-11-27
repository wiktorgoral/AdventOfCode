import copy


def more_common(listt):
    sign_0: int = 0
    sign_1: int = 0
    for i in listt:
        if i == "0":
            sign_0 += 1
        else:
            sign_1 += 1
    return sign_0, sign_1


file1 = open('data.txt', 'r')
matrix = []
size_y: int = 0
size_x: int = 0
line_current: str = ""

while True:
    line_current = file1.readline().rstrip()
    if not line_current:
        break

    matrix.append([])
    matrix[size_y] = ([x for x in line_current])
    size_y += 1
file1.close()
size_x = len(matrix[0])

matrix_criteria_ox = copy.deepcopy(matrix)
count: int = 0
while True:
    common = more_common(list(zip(*matrix_criteria_ox))[count])
    matrix_tmp = copy.deepcopy(matrix_criteria_ox)
    if common[1] >= common[0]:
        for i in range(len(matrix_criteria_ox)):
            if matrix_criteria_ox[i][count] == "0": matrix_tmp[i] = None
    else:
        for i in range(len(matrix_criteria_ox)):
            if matrix_criteria_ox[i][count] == "1": matrix_tmp[i] = None
    matrix_tmp = list(filter(None, matrix_tmp))
    matrix_criteria_ox = matrix_tmp
    count += 1
    if len(matrix_criteria_ox) == 1: break

print(matrix_criteria_ox)

matrix_criteria_co2 = copy.deepcopy(matrix)
count: int = 0
while True:
    common = more_common(list(zip(*matrix_criteria_co2))[count])
    matrix_tmp = copy.deepcopy(matrix_criteria_co2)
    if common[0] < common[1]:
        for i in range(len(matrix_criteria_co2)):
            if matrix_criteria_co2[i][count] == "1": matrix_tmp[i] = None
    elif common[1] < common[0]:
        for i in range(len(matrix_criteria_co2)):
            if matrix_criteria_co2[i][count] == "0": matrix_tmp[i] = None
    elif common[0] == common[1]:
        for i in range(len(matrix_criteria_co2)):
            if matrix_criteria_co2[i][count] == "1": matrix_tmp[i] = None
    matrix_tmp = list(filter(None, matrix_tmp))
    matrix_criteria_co2 = matrix_tmp
    count += 1
    if len(matrix_criteria_co2) == 1: break

print(matrix_criteria_co2)

print(matrix_criteria_ox[0], int("".join(matrix_criteria_ox[0]), 2), matrix_criteria_co2[0], int("".join(matrix_criteria_co2[0]), 2), int("".join(matrix_criteria_ox[0]), 2) * int("".join(matrix_criteria_co2[0]), 2))

