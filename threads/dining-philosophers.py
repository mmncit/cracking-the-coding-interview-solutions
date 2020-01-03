import time

class Chopsticks:
    def __init__(self, n_chopsticks):
        self.chopsticks = [False] * n_chopsticks  # set of chopsticks
        # False: the chopstick is free
        # True: the chopstick is occupied

    def lock_chopstick(self, i):
        self.chopsticks[i] = True

    def release_chopstick(self, i):
        self.chopsticks[i] = False

    def __str__(self):  # current state of free/occupied resources
        return str(self.chopsticks)


class Philosopher:
    def __init__(self, pid, time_to_think=1, time_to_eat=1):
        self.pid = pid  # id of philosopher (indexed from 0)
        self.time_to_think = time_to_think
        self.time_to_eat = time_to_eat

    def think(self):
        print(f"p{self.pid} starts thinking for {self.time_to_think} sec")
        time.sleep(self.time_to_eat)
        print(f"p{self.pid} stops thinking... {self.time_to_think}")

    def take_left_chopstick(self):
        print(f"p{self.pid} takes chopstick index {self.pid}")
        return self.pid

    def take_right_chopstick(self, number_of_chopsticks):
        print(f"p{self.pid} takes chopstick index {(self.pid + 1)% number_of_chopsticks}")
        return (self.pid + 1) % number_of_chopsticks

    def eat(self):
        print(f"p{self.pid} starts eating for {self.time_to_eat} sec")
        time.sleep(self.time_to_eat)
        print(f"p{self.pid} stops eating... {self.time_to_eat}")

    def put_left_chopstick(self):
        print(f"p{self.pid} puts chopstick index {self.pid}")
        return self.pid

    def put_right_chopstick(self, number_of_chopsticks):
        print(f"p{self.pid} puts chopstick index {(self.pid + 1)% number_of_chopsticks}")
        return (self.pid + 1) % number_of_chopsticks


def main():
    n_philosophers = n_chopsticks = 5
    c = Chopsticks(n_chopsticks)   # initialize chopsticks
    for i in range(n_philosophers):
        p = Philosopher(i)
        p.think()
        c.lock_chopstick(p.take_left_chopstick())
        c.lock_chopstick(p.take_right_chopstick(n_chopsticks))
        print(c)
        p.eat()
        c.release_chopstick(p.put_left_chopstick())
        c.release_chopstick(p.put_right_chopstick(n_chopsticks))
        print(c)


if __name__ == '__main__':
    main()
