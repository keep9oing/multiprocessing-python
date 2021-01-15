# 2 types of communication channel
# 1. Queue
# 2. Pipes

from multiprocessing import Process, Queue, Pipe

def q_comm(q):
    q.put([42, None, 'hello'])

def pipe_comm(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == "__main__":

    # # Queue communication
    # q = Queue()
    # p = Process(target = q_comm, args=(q,))
    # p.start()
    # print(q.get())
    # p.join()

    # pipe communication
    parent_conn, child_conn = Pipe()
    p = Process(target=pipe_comm, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()