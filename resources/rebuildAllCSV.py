import sys

path = '../csv'

dirF = open("./granules.txt", "r")
fileF = open("./dataset.txt", "r")
metaF = open("./metadata.txt", "r")

dirArr = []
fileArr = []
metaArr = []

for li in fileF:
    fileArr.append(li.strip())

for li in dirF:
    dirArr.append(li.strip())
    
for li in metaF:
    metaArr.append(li.strip())


def rebuild_CSV(dirName, fileName):
    skip = True
    prevRowInx = 0
    runOnLine = ""
    rows = []
    
    pathToRaw = '{path}/raw/{dir}/{file}'.format(path=path, dir=dirName, file=fileName)
    pathToRebuild = '{path}/rebuilt/{dir}/{file}'.format(path=path, dir=dirName, file=fileName)
    
    for line in open(pathToRaw, 'r'):
        if skip == True:
            skip = False
            continue
            
        splitLine = line.split(':')
        rowInx = splitLine[0].split(',')[0].split('(')[1]
        curData = splitLine[1]

        if prevRowInx == rowInx:
            runOnLine = runOnLine[0:-1] + curData
        else:
            runOnLine = runOnLine[0:-2]
            rows.insert(int(prevRowInx), runOnLine)
            runOnLine = curData

        prevRowInx = rowInx

    with open(pathToRebuild, "w") as f:
        for r in rows:
            f.write(str(r) +"\n")

    #sanity
    colLen = len(rows[0].split(','))
    rowLen = len(rows)
    print('shape: {col} x {row}'.format(col=colLen, row=rowLen))


for dirLi in dirArr:
    print(dirLi)
    
    for fiLi in fileArr:
        print(fiLi)
        rebuild_CSV(dirLi, fiLi + ".csv")
    
    for metLi in metaArr:
        print(metLi)
        rebuild_CSV(dirLi + "/meta", metLi + ".csv")