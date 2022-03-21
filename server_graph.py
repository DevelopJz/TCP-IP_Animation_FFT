import socket 
import numpy as np
import time

t=0
timev=2
tplus=0.1 
w=1000

sig1list=[]
sig2list=[]
sig3list=[]

HOST = '127.0.0.1'
PORT = 8090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen()
print("Server Start")

client_socket, addr = server_socket.accept() 
print("Sending")

while True:
    t=t+tplus
    send_t=str(t)
    
    sig1=np.sin(0.002*np.pi*w*t)
    sig1list.append(sig1)
    send_sig1="C"+str(sig1)
    
    sig2=np.sin(2*0.002*np.pi*w*t)
    sig2list.append(sig2)
    send_sig2="D"+str(sig2)
    
    sig3=sig1+sig2
    sig3list.append(sig3)
    send_sig3="E"+str(sig3)+"F"

    socket_data=(send_t+send_sig1+send_sig2+send_sig3).encode()
    client_socket.sendall(socket_data)
    time.sleep(timev)
            
server_socket.close()