from colorama import Fore, Style

def print_ly(x):
    return print(Fore.LIGHTYELLOW_EX + "CivBrowser: " + x + Style.RESET_ALL )
def print_lc(x):
    return print(Fore.LIGHTCYAN_EX + "CivBrowser: " + x + Style.RESET_ALL )
def print_err(x):
    return print(Fore.RED + "CivBrowser: " + x + Style.RESET_ALL )
def print_n(x):
    return print("CivBrowser: " + x )
