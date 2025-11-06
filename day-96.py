import multiprocessing
import time

def square(n):
    print(f"Square of {n} is {n*n}")
    time.sleep(1)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=square, args=(num,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All processes finished")
