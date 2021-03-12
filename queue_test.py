from multiprocessing import Queue

q = Queue(10)
a = 50
b = 100
q.put(a)
q.put(b)


print(q.get())
print(q.get())