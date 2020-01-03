# ref: https://codewithoutrules.com/2017/08/16/concurrency-python/
from threading import Thread
from threading import Lock


class Counter(object):
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.value += 1

c = Counter()

def go():
    for i in range(1000000):
        c.increment()

# Run two threads that increment the counter:
t1 = Thread(target=go)
t1.start()
t2 = Thread(target=go)
t2.start()
t1.join()
t2.join()
print(c.value)  # 1641767
# value is less than 2000000
