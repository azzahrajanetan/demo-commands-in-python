import os

#with os.chdir('~/house'):
#os.system(create)
    
#add = ("git add .")
#commit = ('"git commit -m "adding to repo using python"')

#check_status = ("git status")

#os.system(add)
#os.system(commit)
#os.system(check_status)

file1 = open('household-items.txt', 'r')
every_item = file1.readlines()

for each_item in every_item:
    os.system(f"touch {each_item.strip()}")

file2 = open('commands.txt', 'r')
every_line = file2.readlines()

for each_line in every_line:
    os.system(f"{each_line.strip()}")

