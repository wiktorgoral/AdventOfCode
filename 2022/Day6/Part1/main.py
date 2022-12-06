file1 = open('data.txt', 'r')
line = file1.readline().rstrip()
file1.close()
sliding_array = [line[0], line[1], line[2], line[3]]
for i in range(4, len(line)):
    sliding_array.pop(0)
    sliding_array.append(line[i])
    if sliding_array[0] != sliding_array[1] and sliding_array[0] != \
        sliding_array[2] and sliding_array[0] != sliding_array[3] and \
        sliding_array[1] != sliding_array[2] and sliding_array[1] != \
        sliding_array[3] and sliding_array[2] != sliding_array[3]:
        print(i)
        break
