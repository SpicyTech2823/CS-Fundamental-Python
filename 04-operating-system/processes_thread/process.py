from multiprocessing import Process
import os


def print_process_info():
    print("Child process ID:", os.getpid())


if __name__ == "__main__":
    print("Main process ID:", os.getpid())

    process = Process(target=print_process_info)

    process.start()
    process.join()

    print("Process completed.")