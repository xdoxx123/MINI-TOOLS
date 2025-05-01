from scapy.all import ARP, Ether, srp
import ipaddress
import colorama
def scan(ip_range):
    print(f"{colorama.Fore.GREEN}[*] Scanning network...\n")

    # Build ARP request
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send and receive
    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    # Print results
    print("IP" + " " * 18 + "MAC")
    print("-" * 40)
    for device in devices:
        print(colorama.Fore.LIGHTCYAN_EX+"{:16}    {}".format(device['ip'], device['mac']))

def get_local_range():
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    # You can hardcode this to something like '192.168.1.0/24' if desired
    net = ipaddress.ip_network(local_ip + "/24", strict=False)
    return str(net)

