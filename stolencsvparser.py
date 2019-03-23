hashesFile = open('stolen.txt', 'r')
hashesFile = hashesFile.read()
hashes = hashesFile.split('\n')

def toString(y): 
    s = ""
    for x in range(len(y)):
        s+=str(y[x])
        if x+1 != len(y):
            s+=","
    return s

hashesFileOperation = open("dataset.csv", "a")
for x in range(len(hashes)):
    hashes[x] = hashes[x].split('|')
    a = list(hashes[x])
    del(a[:2])
    hashesFileOperation.write(toString(a)+'\n')

