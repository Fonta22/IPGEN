from colorama import Fore, Style

def errorMsg():
    print(
    Fore.MAGENTA + '[ ' + Fore.RED + 'ERR' + Fore.MAGENTA + ' ]' + Style.RESET_ALL + ' You must enter an integer number: '+ Fore.YELLOW +'ipgen'+ Fore.MAGENTA +' [num] [-s]'+Style.RESET_ALL
    )