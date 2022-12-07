import os

# create an empty list called 'total'
total = []

# start in the current directory
path = "./Day7FAroundFindOutFolder"

[os.path.join(root,file).replace('./Day7FAroundFindOutFolder/','') if file.endswith('.txt') else None for file in [for root,dirs,files in os.walk(path)]]

[os.path.join(root, file).replace('./Day7FAroundFindOutFolder/','') if file.endswith('.txt') else None for file []]

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            total.append()

# print the contents of the 'total' list
print(total)