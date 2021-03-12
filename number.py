from multiprocessing import Process, Queue



q = Queue(5)
q.put(90)
def hanal():
    a = 0
    for i in range(100):
        a += i
    q.put(a)
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    p = Process(target=hanal)
    p.start()
    p.join()

    print(q.get())
    print(q.get())

