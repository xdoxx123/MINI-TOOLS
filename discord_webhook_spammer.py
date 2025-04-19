import requests
import json
from colorama import Fore, init


init(autoreset=True)

def send_webhook(url, content):
    response = requests.post(url, data=json.dumps({"content": content}), headers={"Content-Type": "application/json"})
    if response.ok:
            print(f"{Fore.GREEN}[+]Request Sent Successfully")
    else:
            print(f"{Fore.RED}[!]Request Sent Unsuccessfully (Status Code: {response.status_code})")
    return response

def send_a_couple_of_requests(url, content, count):
    codes = []
    for _ in range(int(count)):
        response = send_webhook(url, content)
        codes.append(response)

    
        
