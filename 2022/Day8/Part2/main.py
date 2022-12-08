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

score = []

for i in range(1, size - 1):
  score.append([])
  for j in range(1, size - 1):
    # right
    right = 0
    for k in range(j + 1, size):
      right += 1
      if grid[i][j] <= grid[i][k]:
        break
    # left
    left = 0
    for k in range(1, j+1):
      left += 1
      if grid[i][j] <= grid[i][j-k]:
        break
    # top
    top = 0
    for k in range(1, i+1):
      top += 1
      if grid[i][j] <= grid[i-k][j]:
        break
    # bot
    bot = 0
    for k in range(i + 1, size):
      bot += 1
      if grid[i][j] <= grid[k][j]:
        break
    score[i-1].append(right * left * top * bot)

print(max(max(x) for x in score))
