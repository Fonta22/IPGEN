import sys
from ipgenerate import generateIP
from colorama import Fore, Style
from error import errorMsg

saveLoc = './logs/ip.log'

def clearLog():
    open(saveLoc, 'w').close()
    print('[' + Fore.YELLOW + ' Cleared Log ' + Style.RESET_ALL + ']:' + Fore.CYAN + ' \'' + saveLoc + '\' ' + Style.RESET_ALL)
    exit()

try:
    num = int(sys.argv[1])
except ValueError:
    errorMsg()
    exit()
ipArr = generateIP(num)
first = True

if num == 0:
    clearLog()

fl = open(saveLoc, 'w+')
for i in range(num):
    if not first:
        fl.write('\n' + ipArr[i])
    else:
        fl.write(ipArr[i])
        first = False

fl.close()

print('Saved [ ' + Fore.YELLOW + str(num) + Style.RESET_ALL + ' ] IP address at' + Fore.CYAN + ' \'' + saveLoc +'\' ' + Style.RESET_ALL)