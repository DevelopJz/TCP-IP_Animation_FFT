# Python3 연습 과제
## 5-Python3 TCP-IP_Streaming

### 사용 언어
**Python 3.7.6**  
**Anaconda 4.8.2**

### 사용 환경
**Windows**  

### 라이브러리
numpy  
matplotlib  
time  

### 라이브러리 설치
```python

python -m pip install 라이브러리명

```

### 코드 설명
**Animation_Graph.py**  

시간에 따른 사인함수 그래프를 애니메이션으로 그래프 출력  
코드 동작 시 그래프에 시간이 흐름에 따라 데이터 누적으로 그래프 그림  

**Animation_FFT.py**  

시간에 따른 사인함수 그래프와 변하는 데이터에 따라 FFT 그래프 출력  
코드 동작 시 사인함수 그래프 / FFT 그래프 변화

**server_graph.py**  

TCP/IP의 서버 역할, Signal 데이터 클라이언트에 전달  

**client_graph.py**  

TCP/IP의 클라이언트 역할, Signal 데이터 전달 받아 Signal 그래프 / FFT 그래프 작성
