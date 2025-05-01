from colorama import Fore
from . import port_scanner
from . import ip_scanner
from . import utiliy
import keyboard
import time
from . import ddos_tool
import main
from . import discord_webhook_spammer
from . import ippinger
from . import geoip_locator
from . import wifipassviewer
from . import devicescanner
def port_scan_stuff(): 





    utiliy.clear()
    print("\n\n")
    ip = input(f"{Fore.LIGHTCYAN_EX} The Ip Address < \n")
    rang = input(f"{Fore.LIGHTCYAN_EX} Max port to search < \n")
    print(Fore.RESET)
    if(int(rang)):
        utiliy.clear()
        rang = int(rang)
        print(f"{Fore.LIGHTCYAN_EX} Started Port scanning please wait a second...")
        w=port_scanner.scan_ports(ip=ip,port_range=range(1,rang+1))
        print(f"{Fore.LIGHTCYAN_EX}Press r to return to main menu \n")
        print(f"{Fore.LIGHTCYAN_EX}Press 2 to dump \n")
        while True:
            if keyboard.is_pressed("2"):
                
                with open("ports.txt", "w") as file:
                    for port, is_open in sorted(w):
                        if is_open is True:
                            file.write(f"Port {port} is open\n")
                        elif is_open is False:
                            file.write(f"Port {port} is closed\n")
                        else:
                            file.write(f"Port {port} scan error\n")
                print("Done")
                input("Press Enter to continue...")
                main.main()
                break
            if keyboard.is_pressed("r"):
                main.main()
                break
    else:
        utiliy.Error("range is not a number!")


def ip_scan_stuff():
    print("\n\n")
    utiliy.clear()
    

    start_ip = input(f"{Fore.LIGHTCYAN_EX} Starter IP < ")
    end_ip = input(f"{Fore.LIGHTCYAN_EX} End IP < ")


    results = ip_scanner.start_scanning(start_ip=start_ip, end_ip=end_ip)
    
    print("\n")
    print(f"{Fore.LIGHTCYAN_EX}  Press r to return to the menu. \n")
    print(f"{Fore.LIGHTCYAN_EX}  Press 2 to dump the results to a log file. \n")

    while True:
        if keyboard.is_pressed("r"):
            
            utiliy.clear()
            main.main()  
            break
        elif keyboard.is_pressed("2"):
           
           with open("iplogs.txt", "w") as a:
            for result in results:
                ip = result['ip'] 
                status = result['status']  

                print(f"{ip}\n{status}\n")  
                a.write(f"{ip} is {status}\n")  
        
           input("Press Enter to continue")
           utiliy.clear()
           main.main()
            

def ddos_stuff():
    print("\n\n")
    utiliy.clear()
    

    ip = input(f"{Fore.LIGHTCYAN_EX}  IP < ")
    port = input(f"{Fore.LIGHTCYAN_EX} Port < ")
    packet_amount =input(f"{Fore.LIGHTCYAN_EX} Amount < ")
    tasks=input(f"{Fore.LIGHTCYAN_EX} Amount of agents < ")
    type=input(f"{Fore.LIGHTCYAN_EX} Type of the ddos [http,tcp,both] < ")

    print(f"{Fore.LIGHTCYAN_EX} MAY THE SOLAR BEAM FIRED OUT")
    results = ddos_tool.start_ddos(ip,port,packet_amount,tasks,type)
    
    print(f"{Fore.LIGHTCYAN_EX} Succesful")
    print("\n")
    
    

    print(f"{Fore.LIGHTCYAN_EX}  Press r to return to the menu. \n")
    while True:
        if keyboard.is_pressed("r"):
            
            utiliy.clear()
            main.main() 
            break
              




def discord_spam_stuff():
    print("\n\n")
    utiliy.clear()
    
    
    web = input(f"{Fore.LIGHTCYAN_EX}  Webhook < ")
    Content = input(f"{Fore.LIGHTCYAN_EX} Content to be send < ")
    packet_amount =input(f"{Fore.LIGHTCYAN_EX} Amount of requests < ")
    

    print(f"{Fore.LIGHTCYAN_EX} Let the dogs out!")
    results = discord_webhook_spammer.send_a_couple_of_requests(web,Content,packet_amount)
    
    print(f"{Fore.GREEN} Succesful")
    print("\n")
    print(f"{Fore.LIGHTCYAN_EX}  Press r to return to the menu. \n")
    while True:
        if keyboard.is_pressed("r"):
            
            utiliy.clear()
            main.main()  
            break
                 

def ippinger_stuff():
    print("\n\n")
    utiliy.clear()
    

    web = input(f"{Fore.LIGHTCYAN_EX}  Ip to ping < ")
    Content = input(f"{Fore.LIGHTCYAN_EX} how much to ping < ")
    packet_amount =input(f"{Fore.LIGHTCYAN_EX} size in bytes  < ")
    result_list = ippinger.pingrepeat(web,int(Content),int(packet_amount))
    
    for result in result_list:
        print(f"{Fore.GREEN}IP: {result['ip']}, Status: {result['status']}, Response: {result['response']}")
    
    
    print(f"{Fore.LIGHTCYAN_EX}  Press R to return to the menu. \n")
    while True:
        if keyboard.is_pressed("r"):
            
            utiliy.clear()
            main.main() 
            break
              
def geoip_locator_options():
    print("\n\n")
    utiliy.clear()

    ip = input(f"{Fore.LIGHTCYAN_EX} Ip to scan <")
    geoip_locator.geoip_lookup(ip=ip)
    print(f"{Fore.LIGHTCYAN_EX}  Press R to return to the menu. \n")
    while True:
        if keyboard.is_pressed("r"):
            
            utiliy.clear()
            main.main() 
            break


def wifipassviewer_options():
    print("\n\n")
    utiliy.clear()

    profiles =wifipassviewer.get_profiles()

    for a in profiles:
        wow = wifipassviewer.get_password(a)
        print(f"{Fore.GREEN} {a}-{wow}")

    print(f"{Fore.LIGHTCYAN_EX}  Press R to return to the menu. \n")
    while True:
        if keyboard.is_pressed("r"):
            
            utiliy.clear()
            main.main() 
            break

def devicescanner_options():
    print("\n\n")
    utiliy.clear()
    wow=devicescanner.get_local_range()
    try:
        devicescanner.scan(wow)
    except PermissionError:
        print(Fore.RED+"[!] Run as a administator")
        utiliy.clear()
        main.main()
    print(f"{Fore.LIGHTCYAN_EX}  Press R to return to the menu. \n")
    while True:
        if keyboard.is_pressed("r"):
            
            utiliy.clear()
            main.main() 
            break
