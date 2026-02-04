# This packet analyzer is for educational purposes only

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def analyze_packet(packet):
    if IP in packet:
        print("New Packet Captured")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if TCP in packet:
            print("Protocol: TCP")
        elif UDP in packet:
            print("Protocol: UDP")
        else:
            print("Protocol: Other")

        print("-" * 40)

print("Starting packet capture... Press Ctrl+C to stop")
sniff(prn=analyze_packet, count=10)
