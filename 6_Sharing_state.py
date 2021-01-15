# 굳이 shared data를 쓰고 싶을때, (추천 X)

# # 1. Shared memory
# from multiprocessing import Process, Value, Array

# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]

# if __name__ == '__main__':
#     num = Value('d', 0.0) # d: double precisioin
#     arr = Array('i', range(10)) # i: signed integer

#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()

#     print(num.value)
#     print(arr[:])

# 2. Server process
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)