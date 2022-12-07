import os

basepath = './Day7FAroundFindOutFolder'
textfiles = []

for root, dirs, files in os.walk(basepath):
    for file in files:
        if file.endswith(".txt"):
            textfiles.append(os.path.join(root, file).replace(basepath+'/','~/').replace('.txt',''))

with open('log.txt','w') as f:
    for i in textfiles:
        f.write(i+'\n')

foldersizes = {}
for file in textfiles:
    splitted = file.split('/')
    splitlen = len(splitted)
    for folderindex in range(len(splitted[:-1])):
        if splitted[folderindex] in foldersizes:
            foldersizes[splitted[folderindex]] += int(splitted[-1])
        else:
            foldersizes[splitted[folderindex]] = int(splitted[-1])

print(len(foldersizes))

totaldatasize = 0

for folder, size in foldersizes.items():
    if size < 100000:
        totaldatasize += size

print(totaldatasize)
