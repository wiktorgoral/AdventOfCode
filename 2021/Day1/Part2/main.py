file1 = open('data.txt', 'r')
count: int = 1
window: [int] = [0]*3
for i in range(3):
    window[i] = int(file1.readline())
increase_count: int = 0
while True:
    line_next = file1.readline()
    if not line_next:
        break

    if window[1]+window[2]+int(line_next) > sum(window):
        increase_count += 1
    window.pop(0)
    window.append(int(line_next))
    count += 1

file1.close()

print(count, increase_count)
