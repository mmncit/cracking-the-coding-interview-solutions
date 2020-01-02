import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} sec...")
    time.sleep(seconds)
    return f"done sleeping...{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    # context manager
    # f1 = executor.submit(do_something, 1)  # arg = 1
    # print(f1.result())

    secs = [5, 3, 4, 2, 1]

    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #    print(f.result())

    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"finished in {round(finish-start, 2)} seconds(s)")

# finished all the threads in almost 1.5 sec
