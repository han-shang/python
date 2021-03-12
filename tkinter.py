
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,number):
        self.number = number
        super().__init__()

    def run1(self):
        print("run1执行了")

    def run(self):
        for i in range(self.number):
            time.sleep(1)
            print("run执行了")
        self.run1()


    def father(self):
        print("父进程执行了")
if __name__ == '__main__':
    process = MyProcess(3)
    process.start()
    time.sleep(4)
    process.father()

