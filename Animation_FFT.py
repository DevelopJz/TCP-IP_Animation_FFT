# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:45:24 2020

@author: 박종민
"""

#라이브러리
import numpy as np
import matplotlib.pyplot as plt
import time

#초기 시간
t=0
#샘플링 주파수
Fs=10000

#input 주파수
w=1000

#사용 리스트 선언
#타임 값 리스트
tlist=[]

#함수값 리스트
ylist=[]

#fft 후 주파수 값 리스트
fftxlist=[]

#fft 후 크기 값 리스트
fftylist=[]

#그래프 출력용
a=[]
b=[]

#그래프 선언
fig=plt.figure()

while True:
    #서브플롯 설정
    plt.subplot(2,1,1)
        
    #그래프 표시 100개 이상일 때 슬라이드
    if t>100:
        #리스트의 제일 첫번째 인덱스 삭제로 슬라이드
        a.pop(0)
        b.pop(0)
        #그래프 다시 그리기, 슬라이드 표현
        plt.cla()
    
    #입력 함수 정의
    y=np.sin(2*0.001*np.pi*w*t)
    #y=np.random.randint(-100,100)
    y=round(y,3)
    
    #시간의 흐름에 따라 값 추가
    tlist.append(t)
    ylist.append(y)
    a.append(t)
    b.append(y)
    
    #FFT 계산
    #시간 영역->주파수 영역으로 계산
    n=len(ylist)
    k=np.arange(n)
    T=n/Fs
    freq=k/T
    freq=freq[range(int(n/2))]
    
    #FFT 후 진폭->주파수 크기 변환
    ffty=np.fft.fft(ylist)/n
    ffty=ffty[range(int(n/2))]
    ffty=np.abs(ffty) 
        
    #그래프 라벨, 제목, 디자인 설정
    plt.cla()
    plt.subplots_adjust(hspace=0.5)
    plt.title("Signal Graph")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    
    #함수 그래프 출력
    plt.plot(a,b,"b")
    
    #그래프 애니메이션 위한 일시정지
    plt.pause(0.0001)

    #서브플롯 설정
    plt.subplot(2,1,2)
    
    #그래프 라벨, 제목, 디자인 설정
    plt.cla()
    plt.title("FFT Graph")
    plt.xlim(0,Fs/2)
    plt.xlabel("Freq (Hz)")
    plt.ylabel("Y (Freq)")
    
    #FFT 그래프 출력
    plt.plot(freq,ffty,"g")
    
    #그래프 애니메이션 위한 일시정지
    plt.pause(0.0001)
    
    #시간 값 증가
    t=t+0.1
    
    #소수점 삭제
    t=round(t,1)
    
plt.show()
