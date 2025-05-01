import socket

import tools.logo as logo

from colorama import Fore, Back, Style, init
import keyboard
import tools.utiliy as utiliy
import os
import tools.options as options
import time
def main():
    os.system("title mini tools")
    utiliy.clear()
    logo.print_text("MINI TOOLS")
    for i in range(0,3):
        print("\n")
        time.sleep(0.1)
    print(f"{Fore.LIGHTCYAN_EX} 1 --Port Scanner        4-- Discord Webhook Spammer   \n")
    print(f"{Fore.LIGHTCYAN_EX} 2 --Ip Scanner          5-- Ip pinger \n")
    print(f"{Fore.LIGHTCYAN_EX} 3 --DDoS tool           6-- Geoip locator\n")
    print(f"{Fore.LIGHTCYAN_EX} 7 --Wifi Password Viewer(Windows only)          8-- Device Scanner (Needs Administator)\n")
    print(f"{Fore.RED} q --Leave the tool")
    while True:
        if keyboard.is_pressed("1"):
            time.sleep(0.2)
            options.port_scan_stuff()
        elif keyboard.is_pressed("2"):
            time.sleep(0.2)
            options.ip_scan_stuff()
        elif keyboard.is_pressed("3"):
            time.sleep(0.2)
            options.ddos_stuff()
        elif keyboard.is_pressed("q"):
            time.sleep(0.2)
            quit()
        elif keyboard.is_pressed("4"):
            time.sleep(0.2)
            options.discord_spam_stuff()
        elif keyboard.is_pressed("5"):
            time.sleep(0.2)
            options.ippinger_stuff()
        elif keyboard.is_pressed("6"):
            time.sleep(0.2)
            options.geoip_locator_options()
        elif keyboard.is_pressed("7"):
            time.sleep(0.2)
            options.wifipassviewer_options()
        elif keyboard.is_pressed("8"):
            time.sleep(0.2)
            options.devicescanner_options()
            
            
            
            
            
            



if __name__ == "__main__":
    main()


