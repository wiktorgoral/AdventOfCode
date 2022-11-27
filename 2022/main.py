import os
import pathlib

for i in range(1, 25):
    folder_name: str = str(pathlib.Path().resolve())+"/Day" + str(i)
    os.mkdir(folder_name)
    open(folder_name + "/" + "main.py", "w")
    open(folder_name + "/" + "data.txt", "w")
