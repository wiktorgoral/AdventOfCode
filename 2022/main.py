import os
import pathlib

for i in range(2, 26):
    folder_name: str = str(pathlib.Path().resolve()) + "/Day" + str(i)
    os.remove(folder_name + "/" + "main.py")
    os.remove(folder_name + "/" + "data.txt")
    os.mkdir(folder_name + "/Part1")
    os.mkdir(folder_name + "/Part2")
    open(folder_name + "/Part1/" + "main.py", "w")
    open(folder_name + "/Part1/" + "data.txt", "w")
    open(folder_name + "/Part2/" + "main.py", "w")
    open(folder_name + "/Part2/" + "data.txt", "w")
