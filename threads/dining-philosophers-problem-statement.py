import threading
import time
import random


class Philosopher(threading.Thread):

    def __init__(self, name, left_fork, right_fork):
        print(f"{name} has sat down at the table")
        threading.Thread.__init__(self, name=name)
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        print(f"{threading.currentThread().getName()} has started thinking")
        while True:
            time.sleep(random.randint(1, 5))
            print(f"{threading.currentThread().getName()} has finished thinking")
            self.left_fork.acquire()  # get the left fork
            time.sleep(random.randint(1, 5))
            try:
                print(f"{threading.currentThread().getName()} has acquired the left fork")
                self.right_fork.acquire()
                try:
                    print(f"{threading.currentThread().getName()} has acquired both forks, currently eating")
                finally:
                    self.right_fork.release()
                    print(f"{threading.currentThread().getName()} has released the right fork")
            finally:
                self.left_fork.release()
                print(f"{threading.currentThread().getName()} has released the left fork")

def main():
    n = 5  # number of philosophers = number of forks
    fork = [threading.RLock()] * n

    names = ["Plato", "Descartes", "Voltaire", "Socrates", "Konfuzius"]
    philosophers = []
    for i in range(n):
        philosopher = Philosopher(names[i], fork[i], fork[(i+1) % n])
        philosopher.start()
        philosophers.append(philosopher)

    for philosopher in philosophers:
        philosopher.join()


if __name__ == '__main__':
    main()
