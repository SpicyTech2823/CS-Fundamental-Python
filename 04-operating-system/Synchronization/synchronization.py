from threading import Thread, Lock
counter = 0
lock = Lock()
def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
if __name__ == "__main__":
    thread1 = Thread(target=increment_counter)
    thread2 = Thread(target=increment_counter)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Final counter value:", counter)            
