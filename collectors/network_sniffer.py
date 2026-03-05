from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def start_sniffer():
    print("Starting network sniffer...")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffer()