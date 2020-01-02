import time
from multiprocessing import Process


def do_something(seconds):
    print(f"sleeping {seconds} sec...")
    time.sleep(seconds)
    print(f"done sleeping... {seconds}")


def main():
    start = time.perf_counter()

    processes = []
    # Create two process objects
    for _ in range(10):
        p = Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f"finished in {round(finish - start, 2)} seconds(s)")


if __name__ == '__main__':
    main()
