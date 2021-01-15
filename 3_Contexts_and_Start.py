# 3 ways to start a process
# 1. spawn: start fresh python interpreter process
# 2. fork:  fork the python interpereter
# 3. forkserver: swerver process is started. no unnecessary resource inherited

import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == "__main__":

    # # use start method
    # mp.set_start_method('spawn')
    # q = mp.Queue()
    # p = mp.Process(target=foo, args=(q,))
    # p.start()
    # print(q.get())
    # p.join()

    # use context method, allow use multiple start methods in the same program
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()