file1 = open('data.txt', 'r')
line = file1.readline().rstrip()
file1.close()
sliding_array = []
for i in range(14):
    sliding_array.append(line[i])
print(sliding_array)
for i in range(14, len(line)):
    sliding_array.pop(0)
    sliding_array.append(line[i])
    if len(set(sliding_array)) == 14:
        print(i)
        break


