from threading import Thread
import time

def download_file(file_name):
    print(f"Starting download of {file_name}...")
    time.sleep(2)  # Simulate a delay in downloading
    print(f"Finished downloading {file_name}.")

if __name__ == "__main__":
    thread1 = Thread(target=download_file, args=("file1.txt",))
    thread2 = Thread(target=download_file, args=("file2.txt",))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("All downloads completed.")    