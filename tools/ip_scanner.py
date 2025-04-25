import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Function to scan an individual IP address
def scan_ip(ip):
    result = {"ip": str(ip), "status": None}

    try:
        # Try to connect to port 80 (HTTP) or port 22 (SSH)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        result_http = sock.connect_ex((str(ip), 80))  # Check HTTP (port 80)

        # Check if connection was successful
        if result_http == 0:
            result["status"] = f"{Fore.GREEN}Reachable on port 80 (HTTP)"
        else:
            result_ssh = sock.connect_ex((str(ip), 22))  # Check SSH (port 22)
            if result_ssh == 0:
                result["status"] = f"{Fore.CYAN}Reachable on port 22 (SSH)"
            else:
                result["status"] = f"{Fore.RED}Not reachable."

        sock.close()

    except socket.error:
        result["status"] = f"{Fore.RED}Not reachable."

    # Print the result immediately as the scan completes for this IP
    

    return result  # Return the result as a dictionary

# Function to scan a range of IPs
def scan_ip_range(start_ip, end_ip):
    # Convert to IP address objects using ipaddress module
    network = ipaddress.IPv4Network(f"{start_ip}/24", strict=False)  # Use a /24 subnet for simplicity
    ip_range = list(network.hosts())

    # Use ThreadPoolExecutor for concurrent scanning
    with ThreadPoolExecutor(max_workers=40) as executor:
        # map() will immediately execute the scanning function and print results in real-time
        results = list(executor.map(scan_ip, ip_range))

    return results  # Return the list of results

# Example usage
def start_scanning(start_ip, end_ip):
    print(f"{Fore.GREEN}Starting IP scan...")
    results = scan_ip_range(start_ip, end_ip)
    print(f"{Fore.GREEN}Scan completed.")
    for result in results:
            print(f"{result['ip']} - {result['status']}")
    # Return the results list as well
    return results

# Example of how to print results after calling the scan

    # Print the list of results after the scan is done (optional)
    
