import time
import concurrent.futures


def do_something(seconds):
    print(f"sleeping {seconds} sec...")
    time.sleep(seconds)
    return f"done sleeping... {seconds}"


def main():
    start = time.perf_counter()

    processes = []
    # Create two process objects
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 1.5)
        # print(f1.result())
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f"finished in {round(finish - start, 2)} seconds(s)")


if __name__ == '__main__':
    main()
