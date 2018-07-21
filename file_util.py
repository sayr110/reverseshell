import os

# testing:
#path = os.path.expanduser('~/theWorker.txt')
#data = getFileData(path)
#print data
#createFileWithData('/home/john/test1.txt',data)

def getFileData(path):
    with open(path, 'rb') as f:
        data = f.read()
        return data

def createFileWithData(path, data):
    with open(path, 'wb+') as f:
        f.write(data)

