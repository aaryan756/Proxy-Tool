import requests, os
from colorama import Fore, Back, Style
from time import sleep


proxies = []


def socks4():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"
    req = requests.get(url)
    open("temp_file.txt", "a").write(req.text)
    proxy_temp = open("temp_file.txt", "r")
    for proxy in proxy_temp:
        line = proxy.strip("\n")
        if line != "":
            proxies.append(proxy.strip("\n"))
    proxy_temp.close()
    os.remove("temp_file.txt")


def socks5():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
    req = requests.get(url)
    open("temp_file.txt", "a").write(req.text)
    proxy_temp = open("temp_file.txt", "r")
    for proxy in proxy_temp:
        line = proxy.strip("\n")
        if line != "":
            proxies.append(proxy.strip("\n"))
    proxy_temp.close()
    os.remove("temp_file.txt")


def http():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
    req = requests.get(url)
    open("temp_file.txt", "a").write(req.text)
    proxy_temp = open("temp_file.txt", "r")
    for proxy in proxy_temp:
        line = proxy.strip("\n")
        if line != "":
            proxies.append(proxy.strip("\n"))
    proxy_temp.close()
    os.remove("temp_file.txt")


def main():
    if os.path.exists("proxy_list.txt") == True:
        os.remove("proxy_list.txt")

    input_valid = False

    while input_valid == False:
        os.system("cls")
        print(
            Fore.CYAN
            + """
    ▄▀█ ▄▀█ █▀█ █▄█ ▄▀█ █▄░█ ▀ █▀   █▀█ █▀█ █▀█ ▀▄▀ █▄█   ▀█▀ █▀█ █▀█ █░░
    █▀█ █▀█ █▀▄ ░█░ █▀█ █░▀█ ░ ▄█   █▀▀ █▀▄ █▄█ █░█ ░█░   ░█░ █▄█ █▄█ █▄▄"""
        )
        sleep(0.3)
        print(Style.RESET_ALL)

        proxy_input = input(
            """What type of Proxy would you like to generate?
            """
            + Fore.MAGENTA
            + """[1]"""
            + Style.RESET_ALL
            + """Socks4
            """
            + Fore.MAGENTA
            + """[2]"""
            + Style.RESET_ALL
            + """Socks5
            """
            + Fore.MAGENTA
            + """[3]"""
            + Style.RESET_ALL
            + """Http
            Input: """
        )

        if not (proxy_input == "1" or proxy_input == "2" or proxy_input == "3"):
            print(Fore.RED + "Incorrect Input!")
            sleep(1.5)
            continue

        proxy_amount = input("Please enter amount: ")
        if not proxy_input.isdigit():
            print(Fore.RED + "Incorrect Input!")
            sleep(1.5)

            continue

        match proxy_input:
            case "1":
                kiri = open("proxy_list.txt", "a")
                socks4()
                for count, proxy in enumerate(proxies):
                    if count < int(proxy_amount):
                        if len(proxy) <= 3:
                            print(
                                Fore.RED
                                + "Only "
                                + count
                                + " proxies were found! Writing remaining to file."
                            )
                            break
                        kiri.write(proxy + "\n")
                    else:
                        break
                input_valid = True
            case "2":
                kiri = open("proxy_list.txt", "a")
                socks5()
                for count, proxy in enumerate(proxies):
                    if count < int(proxy_amount):
                        if len(proxy) <= 3:
                            print(
                                Fore.RED
                                + "Only "
                                + count
                                + " proxies were found! Writing remaining to file."
                            )
                            break
                        kiri.write(proxy + "\n")
                    else:
                        break
                input_valid = True
            case "3":
                kiri = open("proxy_list.txt", "a")
                http()
                for count, proxy in enumerate(proxies):
                    if count < int(proxy_amount):
                        if len(proxy) <= 3:
                            print(
                                Fore.RED
                                + "Only "
                                + count
                                + " proxies were found! Writing remaining to file."
                            )
                            break
                        kiri.write(proxy + "\n")
                    else:
                        break
                input_valid = True

    print("Completed")


main()
