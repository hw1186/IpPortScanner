# IP and Port Scanner 

### requirement
netifaces
ttkthemes

1. GUI로 IP확인과 Port스캔이 가능한다.
2. 1024개의 스레드를 동시에 생성하므로, 시스템에 부담을 줄 수 있다. 
3. 스캐닝 작업이 병렬로 실행이 되기 때문에 포트는 랜덤하게 정렬이된다.
4. 스레드의 실행 순서에 따라 랜덤하게 정렬이 된다