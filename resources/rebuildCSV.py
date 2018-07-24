
# USAGE: python3 rebuildCSV.py 'dir' 'file.csv'
import sys

rows = []
prevRowInx = 0
runOnLine = ""

dirName = sys.argv[1] 
fileName = sys.argv[2]
path = '../csv'
pathToRaw = '{path}/raw/{dir}/{file}'.format(path=path, dir=dirName, file=fileName)
pathToRebuild = '{path}/rebuilt/{dir}/{file}'.format(path=path, dir=dirName, file=fileName)
#pathToRebuild = './{file}'.format(file=fileName)


for line in open(pathToRaw, 'r'):
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

#debug
colLen = len(rows[0].split(','))
rowLen = len(rows)
sys.stdout.write('shape: {col} x {row}'.format(col=colLen, row=rowLen))
print(rows[1234])
sys.stdout.flush()

