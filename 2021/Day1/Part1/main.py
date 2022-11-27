file1 = open('data.txt', 'r')
count: int = 1
line_current: str = file1.readline()
increase_count: int = 0
while True:
    line_next: str = file1.readline()
    if not line_next:
        break

    if int(line_next) > int(line_current):
        increase_count += 1
    line_current = line_next
    count += 1

file1.close()

print(count, increase_count)
