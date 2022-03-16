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
warning_flag=0
#그래프 출력용
a=[]
b=[]
c=[]
d=[]

#그래프 선언
fig=plt.figure()

while True:
    if warning_flag==0:
        warning_flag=1
    elif warning_flag==1:
        warning_flag=0
    #서브플롯 설정
    plt.subplot(2,1,1)
        
    #그래프 표시 100개 이상일 때 슬라이드
    if t>100:
        #리스트의 제일 첫번째 인덱스 삭제로 슬라이드
        a.pop(0)
        b.pop(0)
        c.pop(0)
        d.pop(0)
        #그래프 다시 그리기, 슬라이드 표현
        plt.cla()
    
    #입력 함수 정의
    y=0.5*np.exp(t*0.05)
    y=round(y,3)
    
    yy=0.5*np.log(t*0.05)
    yy=round(yy,3)
    
    #시간의 흐름에 따라 값 추가
    a.append(t)
    b.append(y)
    c.append(t)
    d.append(yy)
        
    #그래프 라벨, 제목, 디자인 설정
    plt.cla()
    plt.subplots_adjust(hspace=0.5)
    plt.title("Temperature Graph")
    plt.xlabel("Time (s)")
    plt.ylabel("Temp ('C)")
    
    #함수 그래프 출력
    if y>1:
        if warning_flag==0:
            plt.plot(a,b,"b",label="WARNING")
            plt.legend()
        else:
            plt.plot(a,b,"r",label="WARNING")
            plt.legend()
    else:
        plt.plot(a,b,"b")
    
    #그래프 애니메이션 위한 일시정지
    plt.pause(0.0001)

    #서브플롯 설정
    plt.subplot(2,1,2)
    
    #그래프 라벨, 제목, 디자인 설정
    plt.cla()
    plt.title("Dust Graph")
    plt.xlabel("Time (s)")
    plt.ylabel("Dust amount (%)")
    
    #FFT 그래프 출력
    if yy>0:
        if warning_flag==0:
            plt.plot(c,d,"g",label="WARNING")
            plt.legend()
        else:
            plt.plot(c,d,"r",label="WARNING")
            plt.legend()
    else:
        plt.plot(c,d,"g")
    
    #그래프 애니메이션 위한 일시정지
    plt.pause(0.0001)

    #시간 값 증가
    t=t+0.1
    
    #소수점 삭제
    t=round(t,1)
    
plt.show()

