import sys
from ipgenerate import generateIP
from colorama import Fore, Style

saveLoc = '.\\logs\\ip.log'

def clearLog():
    print('[' + Fore.YELLOW + ' Cleared Log ' + Style.RESET_ALL + ']:' + Fore.CYAN + f' \'{saveLoc}\'' + Style.RESET_ALL)
    exit()

num = int(sys.argv[1])
ipArr = generateIP(num)
first = True

if num == 0:
    clearLog()

fl = open(saveLoc, 'w+')
for i in range(num):
    if not first:
        fl.write(f'\n{ipArr[i]}')
    else:
        fl.write(f'{ipArr[i]}')
        first = False

fl.close()

print('Saved [' + Fore.YELLOW + f' {num} ' + Style.RESET_ALL + f'] IP address at' + Fore.CYAN + f' \'{saveLoc}\'' + Style.RESET_ALL)