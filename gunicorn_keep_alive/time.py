import os
import psutil
import time
import requests
import urllib3
import threading
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


session = requests.Session()
http = urllib3.PoolManager()

def req(i):
    url = "http://127.0.0.1:8000/"
    start = time.time()
    res = session.get(url)
    print(f"thread: {i} time cost: {time.time() - start}")
    time.sleep(2)
    return res

def output_net():
    pid = os.getpid()
    proc = psutil.Process(pid)

    while True:
        print("====proc connections====")
        print(f"pid: {pid} ", proc.connections(kind="tcp4"))
        time.sleep(0.1)


def start_debug():
    t = Thread(target=output_net, daemon=True)
    t.start()


def main():
    url = "http://127.0.0.1:8000/"
    # url = "http://127.0.0.1:80/"

    # start_debug()

    # import pdb;pdb.set_trace()
    for i in range(10):
        start = time.time()
        res = http.request("GET", url)
        print(f"time cost: {time.time() - start}")
        time.sleep(10)

    print("requests")

    # with ThreadPoolExecutor(max_workers=10) as w:
    #     res = w.map(req, range(10))
    # for i in range(10):
    #     start = time.time()
    #     res = requests.get(url)
    #     print(f"time cost: {time.time() - start}")

    # start = time.time()
    # res = session.get(url)
    # print(f"time cost: {time.time() - start}")

    print(res)


if __name__ == "__main__":
    main()
