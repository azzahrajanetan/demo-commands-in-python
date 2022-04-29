import os

file1 = open('household-items.txt', 'r')
every_item = file1.readlines()

for each_item in every_item:
    os.system(f"touch {each_item.strip()}")

file2 = open('commands.txt', 'r')
every_line = file2.readlines()

for each_line in every_line:
    os.system(f"{each_line.strip()}")

