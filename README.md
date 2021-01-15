# mutiprocessing-python


출처:https://docs.python.org/3/library/multiprocessing.html#


## 1. Introduction
Pool을 통한 data parallization

## 2. Process Class
Process 생성, start(), join()메서드 사용

## 3. Contexts and start method
start 형식 지정: spawn, fork, fork server

## 4. Exchainging objects
Queue나 Pipe를 이용한 데이터 교환

## 5. Synchronization
lock을 이용한 synchronize

## 6. Sharing state
1. Value, Array를 이용한 공유 메모리 사용
2. Manager()를 이용한 다양한 타입의 데이터 구조 사용, 이기종간 통신도 되지만 1번보다는 느림

## 7. Using a pool of workers
노동자 풀 사용