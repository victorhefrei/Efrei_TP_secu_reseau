from scapy.all import *
ping = ICMP(type=8)
packet = IP(src="10.2.1.220", dst="10.2.1.254")
frame = Ether(src="08:00:27:42:f4:b5", dst="ca:01:05:ad:00:1c")
final_frame = frame/packet/ping
answers, unanswered_packet = srp(final_frame, timeout=10)
print(f"Pong Reçu : {answers[0]}")
