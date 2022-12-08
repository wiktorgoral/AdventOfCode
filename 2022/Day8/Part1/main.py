file1 = open('data.txt', 'r')
grid = []
size: int = 0
line_current: str = ""

while True:
  line_current = file1.readline().rstrip()
  if not line_current:
    break
  grid.append([])
  for i in range(len(line_current)):
    grid[size].append([])
    grid[size][i].append(int(line_current[i]))
  size += 1
file1.close()


count = 4 * size - 4
for i in range(1, size - 1):
  for j in range(1, size - 1):
    # right
    flag_right = True
    for k in range(j + 1, size):
      if grid[i][j] <= grid[i][k]:
        flag_right = False
        break
    if flag_right:
      count += 1
      continue
    # left
    flag_left = True
    for k in range(0, j):
      if grid[i][j] <= grid[i][k]:
        flag_left = False
        break
    if flag_left:
      count += 1
      continue
    # top
    flag_top = True
    for k in range(0, i):
      if grid[i][j] <= grid[k][j]:
        flag_top = False
        break
    if flag_top:
      count += 1
      continue
    # bot
    flag_bot = True
    for k in range(i + 1, size):
      if grid[i][j] <= grid[k][j]:
        flag_bot = False
        break
    if flag_bot:
      count += 1
      continue
print(count)
