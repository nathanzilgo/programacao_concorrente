import so
import threading
from time import sleep
import random

if __name__ == "__main__":
    eating = waiting = 0
    mutex = threading.Lock(1)
    block = threading.Semaphore(0)
    