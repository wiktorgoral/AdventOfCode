file1 = open('data.txt', 'r')
stacks = [['W', 'R', 'F'],
          ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
          ['P', 'M', 'Z', 'N', 'L'],
          ['J', 'C', 'H', 'R'],
          ['C', 'P', 'G', 'H', 'Q', 'T', 'B'],
          ['G', 'C', 'W', 'L', 'F', 'Z'],
          ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'],
          ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
          ['J', 'W', 'H', 'G', 'R', 'S', 'V']]
size: int = 0
line_current: str = ""
lines=[]
flag = False
while True:
  line_current = file1.readline()
  if line_current =="\n":
    flag=True
    continue

  if not line_current:
    break

  if flag:
    lines.append(line_current.strip())
    size+=1
file1.close()

for i in range(size):
  sep = lines[i].split()
  moves = [int(sep[1]), int(sep[3])-1, int(sep[5])-1]
  index = len(stacks[moves[1]])-moves[0]
  for j in range(moves[0]):
    ele = stacks[moves[1]].pop(index)
    stacks[moves[2]].append(ele)


print(stacks)


