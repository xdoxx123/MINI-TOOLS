from scapy.all import sniff
from colorama import Fore

def StartSniffing():
    def packet_callback(packet):
        print(Fore.GREEN+packet.summary())

    sniff(prn=packet_callback, store=0)