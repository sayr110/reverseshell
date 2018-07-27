import os

def getFileData(path):
    try:
        with open(path, 'rb') as f:
            data = f.read()
            return data
    except:
       return None

def createFileWithData(path, data):
    try:
        with open(path, 'wb+') as f:
            f.write(data)
        return "Success create file {}".format(path)
    except:
        return "Failed to create file {}".format(path)



# testing:
# path = os.path.expanduser('~/theWorker123.txt')
# data = getFileData(path)
# print data
#createFileWithData('/home/john/test1.txt',data)