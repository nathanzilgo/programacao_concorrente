import threading
import multiprocessing
import random
import logging
from queue import Queue

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


def log(message):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f"{threadname} - {processname}: {message}")


# Producer
def create(queue: Queue, finished: Queue, max: int):
    finished.put(False)
    for x in range(max):
        v = random.randint(1, 100)
        queue.put(v)
        log(f"Produced {v}")
    finished.put(True)
    log("Finished")


# Consumer
def consume(work: Queue, finished):
    counter = 0
    while True:
        if not work.empty():
            v = work.get()
            log(f"Consuming {counter} : {v}")
            counter += 1
        else:
            if finished.get():
                break
        log("Finished")


def main():
    max = 50
    work = Queue()
    finished = Queue()

    PRODUCER = threading.Thread(target=create, args=(work, finished, max),
                                daemon=True)
    CONSUMER = threading.Thread(target=consume, args=(work, finished))

    PRODUCER.start()
    CONSUMER.start()

    PRODUCER.join()
    log("Producer finished")

    CONSUMER.join()
    log("Consumer finished")


if __name__ == "__main__":
    main()
