import time
import threading

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} sec...")
    time.sleep(seconds)
    print("done sleeping")


threads = []  # empty list of threads
# create threads
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()  # start the thread
    threads.append(t)  # insert the new thread into the list


# wait until finishing the thread(s)
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"finished in {round(finish-start, 2)} seconds(s)")

# finished all the threads in almost 1.5 sec
