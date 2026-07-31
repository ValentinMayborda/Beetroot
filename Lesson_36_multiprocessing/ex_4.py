#PIPE

from multiprocessing import Process, Pipe


def worker_with_pipe(conn):
    while True:
        data = conn.recv()
        if data is None:
            conn.send(None)
            break

        result = sum(i**2 for i in range(data))
        conn.send(result)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe(duplex=True)
    worker = Process(target=worker_with_pipe, args=(child_conn,))
    worker.start()
    for n in [1000, 5000,10_000]:
        parent_conn.send(n)
        result = parent_conn.recv()
        print(f'sum(i^2, i=0..{n}) = {result}')
    parent_conn.send(None)
    print(parent_conn.recv())
    worker.join()
