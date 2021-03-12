from multiprocessing import Process
from multiprocessing import Queue
import time

f = Queue(10)
class Prime(Process):

    def __init__(self,min,max):
        self.min = min
        self.max = max

        super().__init__()



    def prime_number(self,number):
        if number<=1:
            return False
        else:
            for i in range(2,number // 2 + 1):
                if number % i == 0:
                    return False
        return True



    def run(self):

        sum1 = []
        for q in range(self.min,self.max):
            if self.prime_number(q):
                sum1.append(q)

        f.put(sum(sum1))
        print(f.get())

        print(sum(sum1))




if __name__ == '__main__':
    beti = time.time()
    # prime = Prime(1,100001)
    # prime.start()
    # prime.join()
    #4个进程
    objs = []
    for i in range(1,100001,25000):
        p = Prime(i,i+25000)
        objs.append(p)
        p.start()
    for q in objs:
        q.join()


    # time.sleep(5)
    print(f.get())
    # print(f.get())

    end = time.time()
    print("用时：",end - beti)

