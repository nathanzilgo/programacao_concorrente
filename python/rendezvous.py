import threading

la = threading.Lock()
lb = threading.Lock()


def a():
    print("a1")
    lb.release()
    la.acquire()
    print("a2")


def b():
    print("b1")
    la.release()
    lb.acquire()
    print("b2")


if __name__ == "__main__":

    a = threading.Thread(target=a)
    b = threading.Thread(target=b)

    while (True):
        a.start()
        b.start()
