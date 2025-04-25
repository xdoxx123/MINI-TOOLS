import subprocess
import platform
import concurrent.futures

def ping(ip, bytes):
    """Ping a single IP address with a custom packet size in bytes."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    packet_size = f"-l {bytes}" if platform.system().lower() == "windows" else f"-s {bytes}"

    try:
        # Execute the ping command with the specified parameters
        response = subprocess.run(
            ["ping", param, str(1), ip, packet_size], capture_output=True, text=True
        )

        if response.returncode == 0:
            return {"ip": ip, "status": "Success", "response": response.stdout.strip()}
        else:
            return {"ip": ip, "status": "Failed", "response": response.stderr.strip()}
    except Exception as e:
        return {"ip": ip, "status": "Error", "response": str(e)}

def pingrepeat(ip, repeat, bytes):
    """Ping the specified IP address 'repeat' times with a custom packet size in bytes using concurrency."""
    # Create a ThreadPoolExecutor with 10 workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Prepare a list of arguments for each ping
        futures = [executor.submit(ping, ip, bytes) for _ in range(repeat)]
        
        # Collect all ping responses in a list
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        return results

# Example usage
if __name__ == "__main__":
    ip = input("Enter IP address to ping: ")
    repeat = int(input("Enter number of pings: "))
    bytes = int(input("Enter packet size in bytes: "))
    
    # Get the list of ping results
    result_list = pingrepeat(ip, repeat, bytes)
    
    # Print the result list
    for result in result_list:
        print(f"IP: {result['ip']}, Status: {result['status']}, Response: {result['response']}")
