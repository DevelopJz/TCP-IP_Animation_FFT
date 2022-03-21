import socket
import matplotlib.pyplot as plt
import numpy as np

a=[]
d=[]
e=[]
f=[]
tlist=[]
xlist=[]
ylist=[]
zlist=[]

recvsize=1024
Fs=10000

HOST = '127.0.0.1'  
PORT = 8090  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

fig=plt.figure(figsize=(11,7.5))

while True:
    recvdata=client_socket.recv(recvsize)
    data=recvdata.decode()
    sig1index=data.find("C")
    sig2index=data.find("D")
    sig3index=data.find("E")
    lastindex=data.find("F")
    t=float(data[:sig1index])
    sigV1=float(data[sig1index+1:sig2index])
    sigV2=float(data[sig2index+1:sig3index])
    sigV3=float(data[sig3index+1:lastindex])
    
    a.append(t)
    tlist.append(t)

    d.append(sigV1)
    xlist.append(sigV1)
    
    e.append(sigV2)
    ylist.append(sigV2)
    
    f.append(sigV3)
    zlist.append(sigV3)
    if len(a)>100:
        a.pop(0)
        d.pop(0)
        e.pop(0)
        f.pop(0)
    
    plt.subplot(321)
    plt.cla()
    plt.title("Signal Graph")
    plt.xlabel("Time (s)")
    plt.ylabel("X Value")
    plt.plot(a,d,"m")
    plt.pause(0.0001)
    
    n=len(a)
    k=np.arange(n)
    T=n/Fs
    freq=k/T
    freq=freq[range(int(n/2))]
    
    fftx=np.fft.fft(d)/n
    fftx=fftx[range(int(n//2))]
    fftx=np.abs(fftx)
    
    plt.subplot(322)
    plt.cla()
    plt.title("FFT Graph (X)")
    plt.xlim(0,Fs/2)
    plt.xlabel("Freq (Hz)")
    plt.ylabel("X (Freq)")
    plt.plot(freq,fftx,"y")
    plt.pause(0.0001)
    
    plt.subplot(323)
    plt.cla()
    plt.title("Signal Graph")
    plt.xlabel("Time (s)")
    plt.ylabel("Y Value")
    plt.plot(a,e,"m")
    plt.pause(0.0001)
    
    ffty=np.fft.fft(e)/n
    ffty=ffty[range(int(n/2))]
    ffty=np.abs(ffty)
    
    plt.subplot(324)
    plt.cla()
    plt.title("FFT Graph (Y)")
    plt.xlim(0,Fs/2)
    plt.xlabel("Freq (Hz)")
    plt.ylabel("Y (Freq)")
    plt.plot(freq,ffty,"y")
    plt.pause(0.0001)
    
    plt.subplot(325)
    plt.cla()
    plt.title("Signal Graph")
    plt.xlabel("Time (s)")
    plt.ylabel("Z Value")
    plt.plot(a,f,"m")
    plt.pause(0.0001)
    
    fftz=np.fft.fft(f)/n
    fftz=fftz[range(int(n/2))]
    fftz=np.abs(fftz)
    
    plt.subplot(326)
    plt.cla()
    plt.title("FFT Graph (Z)")
    plt.xlim(0,Fs/2)
    plt.xlabel("Freq (Hz)")
    plt.ylabel("Z (Freq)")
    plt.plot(freq,fftz,"y")
    plt.pause(0.0001)
    plt.tight_layout()

plt.show()
client_socket.close()