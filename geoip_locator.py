import requests
from colorama import Fore

def geoip_lookup(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print(f"{Fore.LIGHTGREEN_EX}[+] IP: {data['query']}")
        print(f"{Fore.LIGHTGREEN_EX}[+] Country: {data['country']}")
        print(f"{Fore.LIGHTGREEN_EX}[+] Region: {data['regionName']}")
        print(f"{Fore.LIGHTGREEN_EX}[+] City: {data['city']}")
        print(f"{Fore.LIGHTGREEN_EX}[+] ZIP: {data['zip']}")
        print(f"{Fore.LIGHTGREEN_EX}[+] Lat/Lon: {data['lat']}, {data['lon']}")
        print(f"{Fore.LIGHTGREEN_EX}[+] ISP: {data['isp']}")
        print(f"{Fore.LIGHTGREEN_EX}[+] Org: {data['org']}")
    else:
        print(f"{Fore.RED}[!] Lookup failed.")
