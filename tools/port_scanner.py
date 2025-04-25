import socket
from colorama import Fore
import concurrent.futures

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.4)
        result = sock.connect_ex((ip, port))
        
        sock.close()

        if result == 0:
            return (port, True)
        else:
            return (port, False)
    except socket.error:
        return (port, None)

def scan_ports(ip, port_range, max_threads=100):
    scanned_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in port_range}

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            scanned_ports.append(result)

    for port,value in sorted(scanned_ports):
        if value == True:
            print(f"{Fore.GREEN} Port {port} is open")
        elif value == False:
            print(f"{Fore.RED} Port {port} is closed")
        else:
            print(f"{Fore.YELLOW} Port {port} errored")


    return scanned_ports
