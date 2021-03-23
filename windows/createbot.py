import sys
from colorama import Fore, Style
from ipgenerate import generateIP
from error import errorMsg

try:
    botnum = int(sys.argv[1])
    botsIP = generateIP(botnum)
except (IndexError, ValueError) as e:
    errorMsg()
    exit()


for i in range(botnum):
    print(botsIP[i])