import threading
from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(1, 50):
            print("Child ", i)


print(threading.current_thread().name)

child = PrintThread()
child.start()
print("Started Child Thread!")

for i in range(1, 50):
    print("Main ", i)
