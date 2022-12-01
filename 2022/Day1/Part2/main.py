elves: list[int] = [0]
current_elf: int = 0

with open("data.txt") as f_in:
    lines = f_in.readlines()

for i in range(len(lines) - 1):
    line_current = lines[i]
    if line_current == "\n":
        current_elf += 1
        elves.append(0)
    else:
        elves[current_elf] += int(line_current.strip())
    if not line_current:
        break

top3: int = 0
for i in range(3):
    top3 += max(elves)
    elves.remove(max(elves))
print(top3)
