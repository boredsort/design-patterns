import threading


class ToSynch:
    def __init__(self):
        self.mutex = threading.RLock()
        self.val = 1

    def asynchronized_method(self):
        self.mutex.acquire()
        try:
            self.val += 1
            return self.val
        finally:
            self.mutex.release()
