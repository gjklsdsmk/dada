from requests import get
from threading import Thread
from fake_headers import Headers
from time import sleep
from telebot import TeleBot



# checker = ProxyChecker()
headers = Headers(headers=True)
proxies = set()
bot = TeleBot("7093667487:AAEBK00IkB3W3SW81b2bx7l879tFK-CitWo")
with open("proxy.txt") as file:
    for line in file:
        proxies.add(line.strip())
proxies.remove("")
# get = scraper.get
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
open("good.txt", 'w').close()
f = open("good.txt", 'ab+')



def try_proxy(proxy, id):
    try:
        proxies = {'http': f'http://{proxy.replace("http://", "")}', 'https': f'http://{proxy.replace("http://", "")}'}
        get("https://api.ipify.org", proxies=proxies, headers=headers.generate()).text
        print(f'{bcolors.BOLD + bcolors.OKGREEN + proxy.replace("http://", "")} - HTTP')
        f.write("http://" + proxy.replace("http://", "") + "\n".encode())
    except: 
        try:
            proxies = {'http': f'https://{proxy.replace("http://", "")}', 'https': f'https://{proxy.replace("http://", "")}'}
            get("https://api.ipify.org", proxies=proxies, headers=headers.generate()).text
            print(f'{bcolors.BOLD + bcolors.OKGREEN + proxy.replace("http://", "")} - HTTPS')
            f.write("https://" + proxy.replace("http://", "") + "\n".encode())
        except: 
            try:
                proxies = {'http': f'socks5 ://{proxy.replace("http://", "")}', 'https': f'http://{proxy.replace("http://", "")}'}
                get("https://api.ipify.org", proxies=proxies, headers=headers.generate()).text
                print(f'{bcolors.BOLD + bcolors.OKGREEN + proxy.replace("http://", "")} - SOCKS5')
                f.write("socks5://" + proxy.replace("http://", "") + "\n".encode())
            except:
                print(f'{bcolors.BOLD + bcolors.FAIL + proxy.replace("http://", "")} - INVALID')
    if id == len(proxies):
        sleep(60)
        bot.send_document(6713279525, f.read(), caption="Ну короче вроде всё")





count = 1
for proxy in proxies:
    # try_proxy(proxy, count)
    Thread(target=try_proxy, args=(proxy, count)).start()
    sleep(0.02)
    count += 1
