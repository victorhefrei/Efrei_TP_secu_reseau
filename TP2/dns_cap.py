from scapy.all import sniff, DNS, DNSQR, DNSRR

def process_packet(packet):
    if packet.haslayer(DNS) and packet[DNS].opcode == 0:
        if packet[DNS].qr == 0:
            print(f"Requête DNS détectée pour : {packet[DNSQR].qname.decode('utf-8')}")
        elif packet[DNS].qr == 1:
            print("Réponse DNS détectée")
            for i in range(packet[DNS].ancount):
                answer = packet[DNS].an[i]
                if isinstance(answer, DNSRR):
                    print(f"Nom : {answer.rrname.decode('utf-8')} -> Adresse : {answer.rdata}")

def main():
    print("Capture des paquets...")
    sniff(filter="port 53", prn=process_packet, store=0)

if __name__ == "__main__":
    main()
