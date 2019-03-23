hashesFile = open('stolen.txt', 'r')
hashesFile = hashesFile.read()
hashes = hashesFile.split('\n')
def getOrds(hash):
    y = list(hash)
    s = ''
    for x in range(len(y)):
        s+=str(ord(y[x]))
    return s

hashesFileOperation = open("dataset.csv", "a")
for x in range(len(hashes)):
    hashes[x] = hashes[x].split('|')
    a = list(hashes[x])
    a[1] = getOrds(a[1])
    hashesFileOperation.write(a[1]+','+a[-1]+'\n')

