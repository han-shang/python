from multiprocessing import Process, Queue
import sys

q = Queue(10)

def student():
    item = {}
    while True:
        name, score = q.get()

        if name == 'exit':
            print(item)
            sys.exit()
        elif score > 90:
            item[name] = score




def input_info():
    while True:
        name = input("请输入学生名字:")
        if not name:
            q.put(('exit',0))
            break
        score = int(input("请输入学生成绩："))
        q.put((name, score))

if __name__ == '__main__':

    p = Process(target=student)
    p.start()
    input_info()
