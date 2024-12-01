from scapy.all import sniff, TCP, IP

handshake_tracker = {}

def detect_handshake(packet):
    if packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        ip_layer = packet[IP]
        
        connection_key = (ip_layer.src, ip_layer.dst, tcp_layer.sport, tcp_layer.dport)
        
        if tcp_layer.flags == 'S' or tcp_layer.flags == 'SEC':  # SYN flag, detecte mieux avec "SEC"
            handshake_tracker[connection_key] = 1
            print(f"SYN packet detected from {ip_layer.src}:{tcp_layer.sport} to {ip_layer.dst}:{tcp_layer.dport}")

        elif tcp_layer.flags == 'SA':
            reverse_key = (ip_layer.dst, ip_layer.src, tcp_layer.dport, tcp_layer.sport)
            if handshake_tracker.get(reverse_key) == 1:
                handshake_tracker[reverse_key] = 2
                print(f"SYN-ACK packet detected from {ip_layer.src}:{tcp_layer.sport} to {ip_layer.dst}:{tcp_layer.dport}")
        
        elif tcp_layer.flags == 'A':
            if handshake_tracker.get(connection_key) == 2:
                print(f"Three-way handshake complete between {ip_layer.src}:{tcp_layer.sport} and {ip_layer.dst}:{tcp_layer.dport}")
                handshake_tracker.pop(connection_key, None)

print("Sniffing for SYN-ACK three-way handshake...")
sniff(filter="tcp", iface="enp0s3", prn=detect_handshake)
  
