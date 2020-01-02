import time
import threading

start = time.perf_counter()


def do_something():
    print("sleeping 1 sec...")
    time.sleep(1)
    print("done sleeping")


# create threads
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# start the thread
t1.start()
t2.start()

# wait until finishing the thread
t1.join()
t2.join()

finish = time.perf_counter()

print(f"finished in {round(finish-start, 2)} seconds(s)")

# finished all the threads in 1 sec
