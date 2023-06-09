import os

files = os.listdir("downloads")

for file in files:
    if ".part" in file:
        files.remove(file)

print(files)