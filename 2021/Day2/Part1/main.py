file1 = open('data.txt', 'r')
count_forward: int = 0
count_depth: int = 0
count: int = 0
line_current: str = ""
while True:
    line_current = file1.readline().rstrip()
    if not line_current:
        break

    if "forward" in line_current:
        count_forward += int(line_current[7:])
    if "up" in line_current:
        count_depth += int(line_current[2:])
    if "down" in line_current:
        count_depth -= int(line_current[5:])

    count += 1

file1.close()

print(count, count_forward, count_depth, count_forward * count_depth)
