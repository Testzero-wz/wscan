import threading
import socket
import queue
from lib.io.ColorOutput import *

class PortScan():
    port_queue = queue.Queue()
    TIMEOUT = 1
    host = None

    def __init__(self, host=None, thread_num=100):
        self.threads = [threading.Thread(target=self.get_state) for i in range(thread_num)]
        self.host = host
        pass

    def init_port_queue(self, start, end):
        for i in range(start, end):
            self.port_queue.put(i)

    def start_port_scan(self, start=1, end=1000):
        self.init_port_queue(start, end)
        for t in self.threads:
            t.start()
        self.port_queue.join()

    def __scan(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.TIMEOUT)
        res = sock.connect_ex((self.host, port))
        if res == 0:
            print("[+] Port:%d\tOpen" % port)
        sock.close()

    def get_state(self):
        while not self.port_queue.empty():
            port = self.port_queue.get()
            try:
                self.__scan(port)
            except Exception as e:
                print(e)
            finally:
                self.port_queue.task_done()


test = PortScan("200.200.223.43")
print("[*] Scanning address %s ..." % test.host)
test.start_port_scan()
print("[!] Done!")
