import sys
from ipgenerate import generateIP

try:
    botnum = int(sys.argv[1])
    botsIP = generateIP(botnum)
except IndexError:
    print('You must enter an integer number: [generate [num] [-s]]')
    exit()


for i in range(botnum):
    print(botsIP[i])